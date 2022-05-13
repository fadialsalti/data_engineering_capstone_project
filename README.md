# Data Engineering Capstone Project
This is the seven weeks project to finish the IBM Data Engineering Professional Certificate. In this Capstone project, I will:
- Collect and understand data from multiple sources.
- Design a database and data warehouse.
- Analyze the data and create a dashboard.
- Extract data from OLTP, NoSQL and MongoDB databases, transform it, and load it into the data warehouse.
- Create an ETL pipeline and deploy machine learning models. <br>

This Capstone provides you with practical hands-on experience to demonstrate all of the Data Engineering skills you have picked up in this Professional Certificate program.  <br>

As part of the capstone project, you will assume the role of an Associate Data Engineer who has recently joined the organization. You will be presented with a business challenge that requires building a data platform for retailer data analytics.<br>

In Module 1 you will design the OLTP database for an E-Commerce website, populate the OLTP Database with the provided data, and automate the export of the daily incremental data into the data warehouse.<br>

In Module 2 you will set up a NoSQL database to store the catalog data for an E-Commerce website, load the E-Commerce catalog data into the NoSQL database, and query the E-Commerce catalog data in the NoSQL database.<br>

In Module 3 you will design the schema for a data warehouse based on the schema of the OLTP and NoSQL databases. You’ll then create the schema and load the data into fact and dimension tables,automate the daily incremental data insertion into the data warehouse, and create Cubes and Rollups to make the reporting easier.<br>

In Module 4 you will create a Cognos data source that points to a data warehouse table, create a bar chart of Quarterly sales of cell phones, create a pie chart of sales of electronic goods by category, andcreate a line chart of total sales per month for the year 2020. <br>

In Module 5 you will extract data from OLTP, NoSQL, and MongoDB databases into CSV format. You will then transform the OLTP data to suit the data warehouse schema, and then load the transformed data into the data warehouse. Finally, you will verify that the data is loaded properly.<br>

In the sixth and final module you will use your skills in Big Data Analytics to create a Spark connection to the data warehouse, and then deploy a machine learning model on SparkML for making sales projections.<br>

## Architecture

![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/Readings/data_platform_architecture.png)

SoftCart's online presence is primarily through its website, which customers access using a variety of devices like laptops, mobiles and tablets.

All the catalog data of the products is stored in the MongoDB NoSQL server.

All the transactional data like inventory and sales are stored in the MySQL database server.

SoftCart's webserver is driven entirely by these two databases.

Data is periodically extracted from these two databases and put into the staging data warehouse running on PostgreSQL.

Production data warehouse is on the cloud instance of IBM DB2 server.

BI teams connect to the IBM DB2 for operational dashboard creation. IBM Cognos Analytics is used to create dashboards.

SoftCart uses Hadoop cluster as it big data platform where all the data collected for analytics purposes.

Spark is used to analyse the data on the Hadoop cluster.

To move data between OLTP, NoSQL and the dataware house ETL pipelines are used and these run on Apache Airflow.

## Module 1: 

In this assignment, you will perform three exercises with multiple tasks. But before proceeding with the assignment, you will check the lab environment by starting the MySQL server and then downloading the file database from the given link. The first exercise requires you to design the schema for the OLTP database by storing data like row ID, product ID, customer ID, price, quantity, and time stamp of sale.

In the second exercise, you will load this data into the OLTP database by importing the data in the downloaded file and then listing the tables in the database. You will also write a query to find out the count of records in the tables. In the final exercise, you will automate admin tasks by writing a query to list all the records created in the last 24 hours and then export them to a file. You will also write a bash script that exports records created in the last 24 hours into another file. After performing each task, you will take a screenshot of the command used, and the output obtained and give a name to the screenshot.

#### Commands used to achieve these tasks:

Starting mysql server on IBM's Theia (Developers' Network): `start_mysql`

Creating a database: `create database sales;`

Using this database: `use sales;`

Creating a table with 5 columns: `create table sales_data (product_id INTEGER NOT NULL,
customer_id INTEGER,
price INTEGER,
quantity INTEGER,
timestamp DATETIME);`

Creating an index: `create index ts on sales (timestamp);`

Basic query: `select count(*) from sales_data;`

Bash script to backup the data in a salesdata.sql file: datadump.sh in Module 1
