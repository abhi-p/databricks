# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning">
# MAGIC </div>
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC # Streaming Query Lab
# MAGIC ### Coupon Sales
# MAGIC
# MAGIC Process and append streaming data on transactions using coupons.
# MAGIC
# MAGIC ##### Objectives
# MAGIC 1. Read data stream
# MAGIC 2. Filter for transactions with coupons codes
# MAGIC 3. Write streaming query results to Delta
# MAGIC 4. Monitor streaming query
# MAGIC 5. Stop streaming query
# MAGIC
# MAGIC ##### Classes
# MAGIC - <a href="https://spark.apache.org/docs/latest/api/python/reference/pyspark.ss/api/pyspark.sql.streaming.DataStreamReader.html" target="_blank">DataStreamReader</a>
# MAGIC - <a href="https://spark.apache.org/docs/latest/api/python/reference/pyspark.ss/api/pyspark.sql.streaming.DataStreamWriter.html" target="_blank">DataStreamWriter</a>
# MAGIC - <a href="https://spark.apache.org/docs/latest/api/python/reference/pyspark.ss/api/pyspark.sql.streaming.StreamingQuery.html" target="_blank">StreamingQuery</a>

# COMMAND ----------

# MAGIC %run ./Includes/Classroom-Setup-01.2L

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ### 1. Read data stream
# MAGIC - Set to process 1 file per trigger
# MAGIC - Read from Delta files in the source directory specified by **`DA.paths.sales`**
# MAGIC
# MAGIC Assign the resulting DataFrame to **`df`**.

# COMMAND ----------

df = (spark
      .readStream
      .option("maxFilesPerTrigger", 1)
      .format("delta")
      .load(DA.paths.sales)
     )

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **1.1: CHECK YOUR WORK**

# COMMAND ----------

DA.validate_1_1(df)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 2. Filter for transactions with coupon codes
# MAGIC - Explode the **`items`** field in **`df`** with the results replacing the existing **`items`** field
# MAGIC - Filter for records where **`items.coupon`** is not null
# MAGIC
# MAGIC Assign the resulting DataFrame to **`coupon_sales_df`**.

# COMMAND ----------

from pyspark.sql.functions import col, explode

coupon_sales_df = (df
                   .withColumn("items", explode(col("items")))
                   .filter(col("items.coupon").isNotNull())
                  )

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **2.1: CHECK YOUR WORK**

# COMMAND ----------

DA.validate_2_1(coupon_sales_df.schema)

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ### 3. Write streaming query results to Delta
# MAGIC - Configure the streaming query to write Delta format files in "append" mode
# MAGIC - Set the query name to "coupon_sales"
# MAGIC - Set a trigger interval of 1 second
# MAGIC - Set the checkpoint location to **`coupons_checkpoint_path`**
# MAGIC - Set the output path to **`coupons_output_path`**
# MAGIC
# MAGIC Start the streaming query and assign the resulting handle to **`coupon_sales_query`**.

# COMMAND ----------


coupons_checkpoint_path = f"{DA.paths.checkpoints}/coupon-sales"
coupons_output_path = f"{DA.paths.working_dir}/coupon-sales/output"

coupon_sales_query = (coupon_sales_df
                      .writeStream
                      .outputMode("append")
                      .format("delta")
                      .queryName("coupon_sales")
                      .trigger(processingTime="1 second")
                      .option("checkpointLocation", coupons_checkpoint_path)
                      .start(coupons_output_path))

DA.block_until_stream_is_ready(coupon_sales_query)

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **3.1: CHECK YOUR WORK**

# COMMAND ----------

DA.validate_3_1(coupon_sales_query)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 4. Monitor streaming query
# MAGIC - Get the ID of streaming query and store it in **`queryID`**
# MAGIC - Get the status of streaming query and store it in **`queryStatus`**

# COMMAND ----------

query_id = coupon_sales_query.id
print(query_id)

# COMMAND ----------

query_status = coupon_sales_query.status
print(query_status)

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **4.1: CHECK YOUR WORK**

# COMMAND ----------

DA.validate_4_1(query_id, query_status)

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ### 5. Stop streaming query
# MAGIC - Stop the streaming query

# COMMAND ----------

coupon_sales_query.stop()
coupon_sales_query.awaitTermination()

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **5.1: CHECK YOUR WORK**

# COMMAND ----------

DA.validate_5_1(coupon_sales_query)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 6. Verify the records were written in Delta format

# COMMAND ----------

display(spark.read.format("delta").load(coupons_output_path))

# COMMAND ----------

# MAGIC %md
# MAGIC ### Classroom Cleanup
# MAGIC Run the cell below to clean up resources.

# COMMAND ----------

DA.cleanup()

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC &copy; 2024 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the 
# MAGIC <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/><a href="https://databricks.com/privacy-policy">Privacy Policy</a> | 
# MAGIC <a href="https://databricks.com/terms-of-use">Terms of Use</a> | 
# MAGIC <a href="https://help.databricks.com/">Support</a>