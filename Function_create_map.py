from pyspark.sql import SparkSession
from pyspark.conf import SparkConf
from IPython.display import display
from pyspark.sql.functions import create_map

spark = SparkSession.builder.master("local").appName("Word Count").config("spark.some.config.option", "some-value").getOrCreate()
array_data = [
    ('John',4,2),
    ('John',6,2),
    ('David',7,3),
    ('John',7,3),
    ('Mike',3,4),
    ('David',5,2),
    ('John',9,7),
    ('David',1,8),
    ('David',4,9),
    ('David',7,4),
    ('Mike',8,5),
    ('Mike',5,2),
    ('Mike',3,8),
    ('John',2,7),
    ('David',1,9)   
]

array_schema = ['Name','Score1','Score2']
array_df = spark.createDataFrame(data = array_data,schema = array_schema)
df_with_col = array_df.withColumn('Map',create_map(array_df['Name'],array_df['Score1']))
df_with_col.show()
display(df_with_col)