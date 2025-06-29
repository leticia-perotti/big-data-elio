from pyspark.sql import SparkSession
import time

spark = SparkSession.builder \
    .appName("Process CSV") \
    .master("spark://spark-master:7077") \
    .getOrCreate()

start = time.time()


df = spark.read.option("header", "true").csv("hdfs://namenode:8020/user/spark/bases/dados_sinteticos_1000000.csv")
df.groupBy("categoria").count().show()

end = time.time()
print(f"Tempo de processamento CSV: {end - start:.2f} segundos")

spark.stop()
