from pyspark.sql import SparkSession
import time

spark = SparkSession.builder \
    .appName("Process JSON por Cliente") \
    .master("spark://spark-master:7077") \
    .getOrCreate()

start = time.time()

df = spark.read.option("header", "true").option("inferSchema", "true").json("hdfs://namenode:8020/user/spark/bases/dados_sinteticos_1000000.json")

df.groupBy("cliente_id").count().show()

end = time.time()
print(f"Tempo de processamento CSV: {end - start:.2f} segundos")

spark.stop()
