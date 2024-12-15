from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, isnan, when
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = spark.read.csv("/data/netflix_titles.csv", header=True, inferSchema=True)

# Show the first 5 rows
df.show(5)
# Load the dataset
df = spark.read.csv("/data/netflix_titles.csv", header=True, inferSchema=True)

# Show the first 5 rows
df.show(5)
# Get the schema of the dataset
df.printSchema()

# Get the number of rows and columns
num_rows = df.count()
num_cols = len(df.columns)
print(f"Number of Rows: {num_rows}")
print(f"Number of Columns: {num_cols}")

# List all column names
print(f"Columns: {df.columns}")
# Get summary statistics of numerical columns
df.describe().show()
# Show unique values in 'type' column
df.select("type").distinct().show()

# Count the number of each type (movie or tv show)
df.groupBy("type").count().show()

# Analyze distribution of 'rating' values
df.groupBy("rating").count().show()
