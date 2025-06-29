from pyspark.sql import SparkSession
import time

spark = SparkSession.builder \
    .appName("Process JSON") \
    .master("spark://spark-master:7077") \
    .getOrCreate()

start = time.time()

df = spark.read.json("hdfs://namenode:8020/user/spark/bases/dados_sinteticos_1000000.json")
df.groupBy("categoria").count().show()

end = time.time()
print(f"Tempo de processamento JSON: {end - start:.2f} segundos")

spark.stop()
