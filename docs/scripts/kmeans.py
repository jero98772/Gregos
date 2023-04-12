from pyspark.sql import SparkSession
from pyspark.ml.linalg import Vector
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.clustering import KMeans
from pyspark.ml.evaluation import ClusteringEvaluator 
import pyspark.sql.functions as f

spark=SparkSession.builder.getOrCreate()
df=spark.read.csv("chess_openings.csv",inferSchema=True,header=True)
df.show()
df.count()
df.createOrReplaceTempView("chess_opening")
spark.sql("select opening_name from chess_opening").show()
spark.sql("select count( DISTINCT opening_name) from chess_opening").show()

data= df.select("moves").rdd.flatMap(lambda x: x).collect()
print(data)
k=1477
kmeans=KMeans(k=k).fit(data)
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