from pyspark.sql import SparkSession
from pyspark import  SparkContext
from pyspark.ml.linalg import Vector
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.clustering import KMeans
from pyspark.ml.evaluation import ClusteringEvaluator 
from pyspark.ml.feature import OneHotEncoder, StringIndexer
from pyspark.ml import Pipeline
from pyspark.sql.functions import col, udf
from pyspark.sql.types import ArrayType,StringType
import pyspark.pandas as ps

def uci2algebraic(move:str,board:chess.Board()):
  """
  convert from uci notation to algebraic notation
  """
  movef=chess.Move.from_uci(move)
  return board.san(movef)

SparkContext.setSystemProperty('spark.executor.memory', '60g')
sc = SparkContext("local", "App Name")
print(sc._conf.get('spark.executor.memory'))

spark=SparkSession.builder.getOrCreate()
df=spark.read.csv("chess_openings.csv",inferSchema=True,header=True).limit(5000)

split = udf(lambda x:x.split(),ArrayType(StringType())) 
#df=df.withColumn("moves", split(col("moves")))


df.show()
df.count()
df.createOrReplaceTempView("chess_opening")
spark.sql("select opening_name from chess_opening").show()
spark.sql("select count( DISTINCT opening_name) from chess_opening").show()
data=df
indexer = StringIndexer(inputCol="moves", outputCol="movesIndex")
indexed = indexer.fit(df).transform(df)
encoder = OneHotEncoder(inputCol="movesIndex", outputCol="movesVec")

assembler = VectorAssembler(inputCols=['movesVec'], outputCol="features")
pipeline = Pipeline(stages=[indexer, encoder, assembler])
model = pipeline.fit(data)
data = model.transform(data)


k=908

kmeans = KMeans(k=k, seed=1)
model = kmeans.fit(data)

centers = model.clusterCenters()

predictions = model.transform(data)

predictions.show()

evaluator = ClusteringEvaluator()

silhouette_score = evaluator.evaluate(predictions)
print("Silhouette with squared euclidean distance = " + str(silhouette_score))