# Databricks notebook source
# MAGIC %md
# MAGIC # San Francisco Crime Analysis using Spark SQL and K-Means
# MAGIC
# MAGIC ## Objective
# MAGIC
# MAGIC The objective of this project is to analyze historical crime incidents in San Francisco from 2003 to 2018 using Spark SQL and machine learning techniques. The analysis focuses on:
# MAGIC
# MAGIC 1. Crime category distribution
# MAGIC 2. District-level crime patterns
# MAGIC 3. Temporal crime trends
# MAGIC 4. Spatial crime hotspots using K-Means clustering
# MAGIC
# MAGIC The findings can help understand crime behaviour and support data-driven public safety decisions.

# COMMAND ----------

df = spark.table("workspace.default.sf_crime")

display(df.limit(10))

print("Rows:", df.count())
print("Columns:", len(df.columns))

# COMMAND ----------

crime_top10 = (
    df.groupBy("Category")
      .count()
      .orderBy("count", ascending=False)
      .limit(10)
)

display(crime_top10)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Dataset Preview
# MAGIC
# MAGIC The dataset contains historical crime incidents reported by the San Francisco Police Department.
# MAGIC
# MAGIC Each record includes crime category, location, date, time, police district and other relevant information.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Insight
# MAGIC
# MAGIC Property-related crimes dominate the dataset. LARCENY/THEFT is by far the most common crime category, suggesting theft prevention should be a key focus of law enforcement.

# COMMAND ----------

district = (
    df.groupBy("PdDistrict")
      .count()
      .orderBy("count", ascending=False)
)

display(district)

# COMMAND ----------

dow = (
    df.groupBy("DayOfWeek")
      .count()
      .orderBy("count", ascending=False)
)

display(dow)

# COMMAND ----------

from pyspark.sql.functions import year

yearly = (
    df.groupBy(year("Date").alias("Year"))
      .count()
      .orderBy("Year")
)

display(yearly)

# COMMAND ----------

from pyspark.sql.functions import hour

hourly = (
    df.groupBy(hour("Time").alias("Hour"))
      .count()
      .orderBy("Hour")
)

display(hourly)

# COMMAND ----------

df.printSchema()

# COMMAND ----------

spatial_df = (
    df.select("X", "Y")
      .dropna()
      .filter("X != 0")
      .filter("Y != 0")
)

print(spatial_df.count())

# COMMAND ----------

from pyspark.ml.feature import VectorAssembler

assembler = VectorAssembler(
    inputCols=["X", "Y"],
    outputCol="features"
)

data = assembler.transform(spatial_df)

# COMMAND ----------

from pyspark.ml.clustering import KMeans

kmeans = KMeans(
    k=5,
    seed=42,
    featuresCol="features"
)

model = kmeans.fit(data)

clusters = model.transform(data)

# COMMAND ----------

centers = model.clusterCenters()

for i, center in enumerate(centers):
    print(f"Cluster {i}: {center}")

# COMMAND ----------

cluster_count = (
    clusters.groupBy("prediction")
            .count()
            .orderBy("count", ascending=False)
)

display(cluster_count)

# COMMAND ----------

from pyspark.ml.feature import VectorAssembler
from pyspark.ml.clustering import KMeans


spatial_df = (
    df.select("X", "Y")
      .dropna()
      .filter((df.X > -123) & (df.X < -122))
      .filter((df.Y > 37) & (df.Y < 38))
)

assembler = VectorAssembler(
    inputCols=["X", "Y"],
    outputCol="features"
)

data = assembler.transform(spatial_df)

kmeans = KMeans(
    k=5,
    seed=42,
    featuresCol="features"
)

model = kmeans.fit(data)

clusters = model.transform(data)

# COMMAND ----------

sample = (
    clusters
    .select("X", "Y", "prediction")
    .sample(False, 0.005, 42)   # 0.5%
)

display(sample)

# COMMAND ----------

centers = model.clusterCenters()

for i, center in enumerate(centers):
    print(f"Cluster {i}: {center}")
