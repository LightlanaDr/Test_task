import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

data = [["1", "Name1"],
        ["2", "Name2"],
        ["3", "Name3"],
        ["4", "Name4"],
        ["5", "Name5"]]

columns = ['productId', 'productName', 'Company']

df = spark.createDataFrame(data, columns)

data2 = [["1", "Cat1", "3"],
        ["2", "Cat2", "4"],
        ["3", "Cat3", "1"]]

columns2 = ['catId ', 'catName', 'productId']



df2 = spark.createDataFrame(data2, columns2)

df.join(df2, df.productId == df2.productId, "outer").show()