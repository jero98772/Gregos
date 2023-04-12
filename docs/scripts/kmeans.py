from pyspark.sql import SparkSession
from pyspark.ml.linalg import Vector
from pyspark.ml.feature import VectorAssembler


spark=SparkSession.builder.getOrCreate()
df=spark.read.csv("chess_openings.csv",inferSchema=True,header=True)
df.show()
df.count()
df.createOrReplaceTempView("chess_opening")
spark.sql("select count(opening_name) from chess_opening").show()
spark.sql("select count( DISTINCT opening_name) from chess_opening").show()
#1477
df.printSchema()
df.describe()

vec_assembler=VectorAssembler(inputCols="moves",outputCol="opening_name")
vec_assembler.transform(df)
#a=set(df["opening_name"])
#print(a)
#print(len(a))