from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder \
    .appName("PySpark Data Processing") \
    .getOrCreate()

# Sample financial data in a list of dictionaries
financial_data = [
    {"date": "2023-01-01", "stock_price": 100, "volume": 5000, "revenue": 100000, "profit": 5000},
    {"date": "2023-01-02", "stock_price": 105, "volume": 7000, "revenue": 120000, "profit": 6000},
    {"date": "2023-01-03", "stock_price": 110, "volume": 6000, "revenue": 110000, "profit": 5500},
    # Add more data...
]

# Create a Spark DataFrame from the financial data
financial_df = spark.createDataFrame(financial_data)

# Perform data processing using PySpark (e.g., aggregation, transformation, cleaning)
# Example: Calculate average stock price, total volume, etc.

# Show the processed data
financial_df.show()

# Stop Spark session
spark.stop()
