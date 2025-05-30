# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning">
# MAGIC </div>
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ## Automate Production Workflows
# MAGIC This module is part of the Data Engineer Learning Path by Databricks Academy.
# MAGIC
# MAGIC #### Lessons
# MAGIC Lecture: Introduction to the REST API and CLI <br>
# MAGIC [ADE 6.1 - Demo - Generate Tokens]($./ADE 6.1 - Generate Tokens) <br>
# MAGIC [ADE 6.2 - Demo - Using the Databricks CLI]($./ADE 6.2 - Using the Databricks CLI) <br>
# MAGIC Lecture: Batch and Streaming Jobs <br>
# MAGIC [ADE 6.3 - Demo - Using the Databricks API]($./ADE 6.3 - Using the Databricks API) <br>
# MAGIC [ADE 6.4 - Demo - Deploy a Pipeline with the CLI]($./ADE 6.4 - Deploy a Pipeline with the CLI) <br>
# MAGIC [ADE 6.5L - Deploy Pipeline with the CLI Lab]($./ADE 6.5L - Deploy Pipeline with the CLI Lab) <br>
# MAGIC Lecture: Working with Terraform <br>
# MAGIC
# MAGIC #### Prerequisites
# MAGIC * Ability to perform basic code development tasks using the Databricks Data Engineering & Data Science workspace (create clusters, run code in notebooks, use basic notebook operations, import repos from git, etc)
# MAGIC * Intermediate programming experience with PySpark
# MAGIC   * Extract data from a variety of file formats and data sources
# MAGIC   * Apply a number of common transformations to clean data
# MAGIC   * Reshape and manipulate complex data using advanced built-in functions
# MAGIC * Intermediate programming experience with Delta Lake (create tables, perform complete and incremental updates, compact files, restore previous versions etc.)
# MAGIC * Beginner experience configuring and scheduling data pipelines using the Delta Live Tables (DLT) UI
# MAGIC * Beginner experience defining Delta Live Tables pipelines using PySpark
# MAGIC   * Ingest and process data using Auto Loader and PySpark syntax
# MAGIC   * Process Change Data Capture feeds with APPLY CHANGES INTO syntax
# MAGIC   * Review pipeline event logs and results to troubleshoot DLT syntax
# MAGIC
# MAGIC
# MAGIC #### Technical Considerations
# MAGIC * This course runs on DBR 14.3.x-scala2.12.
# MAGIC * This course cannot be delivered on Databricks Community Edition.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC &copy; 2024 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the 
# MAGIC <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/><a href="https://databricks.com/privacy-policy">Privacy Policy</a> | 
# MAGIC <a href="https://databricks.com/terms-of-use">Terms of Use</a> | 
# MAGIC <a href="https://help.databricks.com/">Support</a>