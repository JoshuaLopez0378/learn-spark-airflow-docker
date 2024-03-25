print("=== hello starting task ===")
from pyspark.sql import SparkSession
import pyspark
import pandas as pd    
import os 

print ("=== Cur disr ===")
current_working_directory = os.getcwd()
print(current_working_directory)
for filename in os.listdir(current_working_directory):
    if filename.endswith('.txt'):
        with open(os.path.join(current_working_directory, filename)) as f:
            print(f.read())

data = [['Scott', 50], ['Jeff', 45], ['Thomas', 54],['Ann',34]] 
 
# Create the pandas DataFrame 
pandasDF = pd.DataFrame(data, columns = ['Name', 'Age']) 
  
# print dataframe. 
print(pandasDF)



# spark = SparkSession.builder.appName("PythonWordCount").getOrCreate()
spark = SparkSession.builder \
.master("local[1]") \
.appName("sparktest") \
.getOrCreate()

sparkDF=spark.createDataFrame(pandasDF) 
sparkDF.printSchema()
sparkDF.show()
print("=== Extracting Excel ===")
edf = pd.read_excel("./resources/TestExcelFile1.xlsx")
print(edf)

# text = "Hello Spark Hello Python Hello Airflow Hello Docker and Hello Yusuf"

# words = spark.sparkContext.parallelize(text.split(" "))

# wordCounts = words.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)

# for wc in wordCounts.collect():
#     print(wc[0], wc[1])

spark.stop()