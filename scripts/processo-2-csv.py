from pyspark.sql import SparkSession
import time

spark = SparkSession.builder \
    .appName("Process CSV por Cliente") \
    .master("spark://spark-master:7077") \
    .getOrCreate()

start = time.time()

df = spark.read.option("header", "true").option("inferSchema", "true").csv("hdfs://namenode:8020/user/spark/bases/dados_sinteticos_1000000.csv")

df.printSchema()
df.show(5)

df.groupBy("cliente_id").count().show()

end = time.time()
print(f"Tempo de processamento CSV: {end - start:.2f} segundos")

spark.stop()
