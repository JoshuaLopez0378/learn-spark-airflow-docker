import pandas as pd    
data = [['Scott', 50], ['Jeff', 45], ['Thomas', 54],['Ann',34]] 
 
# Create the pandas DataFrame 
pandasDF = pd.DataFrame(data, columns = ['Name', 'Age']) 
  
# print dataframe. 
print(pandasDF)

from pyspark.sql import SparkSession
#Create PySpark SparkSession
spark = SparkSession.builder \
    .master("local[1]") \
    .appName("SparkByExamples.com") \
    .getOrCreate()
#Create PySpark DataFrame from Pandas
sparkDF=spark.createDataFrame(pandasDF) 
sparkDF.printSchema()
sparkDF.show()