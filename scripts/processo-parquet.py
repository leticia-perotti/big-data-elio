from pyspark.sql import SparkSession
import time

spark = SparkSession.builder \
    .appName("Process Parquet") \
    .master("spark://spark-master:7077") \
    .getOrCreate()

start = time.time()

df = spark.read.parquet("hdfs://namenode:8020/user/spark/bases/dados_sinteticos_1000000.parquet")
df.groupBy("categoria").count().show()

end = time.time()
print(f"Tempo de processamento Parquet: {end - start:.2f} segundos")

spark.stop()
