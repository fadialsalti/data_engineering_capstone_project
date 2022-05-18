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

## Module 2:

In this assignment, you will perform a series of tasks in a single exercise. But before proceeding with the assignment, you will install the 'mongoimport' and 'mongoexport' in the lab environment and then download the JavaScript Object Notation (JSON) file. The exercise requires you to first import the JSON file to the MongoDB server into a database and a collection (electronics), then list out all the databases and the collections in the database catalog. Next, you will list the first five documents in the collection, and then you will write a query to find the count of laptops, the number of mobile phones with a screen size of 6 inches, and the average screen size of smartphones. Finally, you will export the ID, type, and model fields from the collection into a Comma Separated Values (CSV) file. 

Task 1 - Import 'catalog.json' into mongodb server into a database named 'catalog' and a collection named 'electronics': `mongoimport -u root -p MTk5NDQtZW5nZmFk --authenticationDatabase admin --db catalog --collection electronics --file catalog.json`

Task 2 - List out all the databases: `show dbs;`

Task 3 - List out all the collections in the database catalog: `use catalog; list collections;`

Task 4 - Create an index on the field "type": `db.electronics.createIndex( { type: 1 } );`

Task 5 - Write a query to find the count of laptops: `db.electronics.count({"type" : "laptop"});`

Task 6 - Write a query to find the number of smart phones with screen size of 6 inches: `db.electronics.count({"type" : "smart phone", "screen size" : 6});`

Task 7. Write a query to find out the average screen size of smart phones: `db.electronics.aggregate([{$group: {_id:"$type", average_screen_size: {$avg:"$screen size"} } }])`

Task 8 - Export the fields _id, "type", "model", from the 'electronics' collection into a file named electronics.csv: 
`mongoexport -u root -p MTkyOTMtZW5nZmFk --authenticationDatabase admin --db catalog --collection electronics --out electronics.csv --type=csv --fields _id,type,model`

## Module 3

Data Warehousing and Data Warehousing Reporting
Assignment Overview

The Assignment is split into two parts - Data Warehousing and Data Warehousing Reporting
Data Warehousing

In this first part of the assignment, you will perform a couple of exercises. But before proceeding with the assignment, you will create an instance of IBM DB2 on the cloud by following the instructions given in the link provided. If you have already created an instance in previous labs, you can continue using that to perform the exercises. The first exercise requires you to design a data warehouse. The e-commerce company has provided you with sample data. You will start your project by designing a Star Schema for the warehouse by identifying the columns for the various dimension and fact tables in the schema. You will name your database as softcart and then use the ERD design tool to design the table softcartDimDate using fields such as DateID, Month, Monthname, and so on. The company would like to have the ability to generate the report on a yearly, monthly, daily, and weekday basis.

The following tasks require you to design the dimension tables softcartDimCategory, softcartDimCountry, and softcartFactSales using the ERD design tool. Finally, you will use the ERD design tool to design the required relationships (one-to-one, one-to-many, and so on) amongst the tables. After performing each task, you will take a screenshot of the entire ERD clearly showing all the field names, data types, and relationships amongst the tables.

In the second exercise, you will load the data into the data warehouse. Your senior Data Engineer has reviewed your design and made a few improvements to your schema design. The data as per the improved schema is available at a link. You will download the data and restore it into a database named staging using the pgAdmin tool. After performing this task, you will take a screenshot showing the success of data restoration.
Data Warehousing Reporting

In this second part of the assignment, you will perform a couple of exercises. But before proceeding with the assignment, you will create an instance of IBM DB2 on the cloud by following the instructions given in the link provided. If you have already created an instance in previous labs, you can continue using that to perform the exercises. The first exercise requires you to load the data provided by the company into the tables in CSV format by performing a series of tasks. You will start by downloading the data from the links provided and then load that data into the DimDate table, DimCategory table, DimCountry table, and fact table FactSales. After loading the data, you will take a screenshot of the first five rows in each table and name the screenshot.

In the second exercise, you will query the loaded data by creating a grouping sets query, rollup query, and cube query using the columns Orderid*, Category, and Price collected. Finally, you will create an MQT named Total_sales_per_country using the country and total sales columns. After performing each task, you will take a screenshot of the SQL and the output rows and then name the screenshot.

The design of the warehouse through the ERP tool in pgadmin is as following:
![](https://github.com/fadialsalti/data_engineering_capstone_project/blob/main/Module%201/warehouse2.png)

After loading the data into db2 on IBM cloud, I solved the following tasks:
Task 5 - Create a grouping sets query using the columns country, category, totalsales: 
```sql
select country, category, sum(amount) as total_sales
from factsales
left join dimcountry
on factsales.countryid = dimcountry.countryid
left join dimcategory
on factsales.categoryid = dimcategory.categoryid
group by grouping sets (country, category);
```
Task 6 - Create a rollup query using the columns year, country, and totalsales:
```sql
select country, year, sum(amount) as total_sales
from factsales
left join dimcountry
on factsales.countryid = dimcountry.countryid
left join dimdate
on factsales.dateid = dimdate.dateid
group by rollup (country, year);
```
Task 7 - Create a cube query using the columns year, country, and average sales:
```sql
select country, year, avg(amount) as average_sales
from factsales
left join dimcountry
on factsales.countryid = dimcountry.countryid
left join dimdate
on factsales.dateid = dimdate.dateid
group by cube (country, year);
```
Task 8 - Create an MQT named total_sales_per_country that has the columns country and total_sales:
```sql
CREATE TABLE total_sales_per_country (country, total_sales) AS
(
select country, sum(amount) as total_sales
from factsales
left join dimcountry
on factsales.countryid = dimcountry.countryid
group by country)
     DATA INITIALLY DEFERRED
     REFRESH DEFERRED
     MAINTAINED BY SYSTEM;
     
refresh table total_sales_per_country;

select * from total_sales_per_country;
```
