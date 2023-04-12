from pyspark.sql import SparkSession
from pyspark import  SparkContext
from pyspark.ml.linalg import Vector
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.clustering import KMeans
from pyspark.ml.evaluation import ClusteringEvaluator 
from pyspark.ml.feature import OneHotEncoder, StringIndexer
from pyspark.ml import Pipeline
SparkContext.setSystemProperty('spark.executor.memory', '60g')
sc = SparkContext("local", "App Name")
print(sc._conf.get('spark.executor.memory'))

spark=SparkSession.builder.getOrCreate()
df=spark.read.csv("chess_openings.csv",inferSchema=True,header=True).limit(10000)
#df=df.limit(10).collect()
df.show()
df.count()
df.createOrReplaceTempView("chess_opening")
spark.sql("select opening_name from chess_opening").show()
spark.sql("select count( DISTINCT opening_name) from chess_opening").show()
data=df
indexer = StringIndexer(inputCol="moves", outputCol="movesIndex")
indexed = indexer.fit(df).transform(df)
encoder = OneHotEncoder(inputCol="movesIndex", outputCol="movesVec")
#encoded = encoder.transform(indexed)
assembler = VectorAssembler(inputCols=['movesVec'], outputCol="features")
pipeline = Pipeline(stages=[indexer, encoder, assembler])
model = pipeline.fit(data)
data = model.transform(data)


k=1178

kmeans = KMeans(k=k, seed=1)
model = kmeans.fit(data)

centers = model.clusterCenters()

predictions = model.transform(data)

predictions.show()

#model=kmeans.fit(df)
#model.transform("e4 e5 d4 d4").groupBy("prediction").count().show()
print(model)

"""df.printSchema()
df.describe()
le = SparkLabelEncoder()
le.fit(y)
vec_assembler=VectorAssembler(inputCols="moves",outputCol="opening_name")
vec_assembler.transform(df)
"""
#a=set(df["opening_name"])
#print(a)
#print(len(a))