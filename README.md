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
![](https://github.com/fadialsalti/data_engineering_capstone_project/blob/main/all_files/warehouse2.png)

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

## Module 4
In this assignment, you will perform a couple of exercises with multiple tasks. But before proceeding with the assignment, you will check the lab environment by ensuring that you have access to a cloud instance of the IBM DB2 database and Cognos. After you have access to the cloud instance, you will download the data from the link provided. The exercise requires you to load data into the data warehouse. You will first import data from the downloaded CSV file into a table and then list the first ten rows in the table.

In the second exercise, you will create a data source in Cognos that points to the table in your IBM DB2 database. In the final exercise, you will create a dashboard by performing tasks such as creating a bar chart of Quarterly sales of mobile phones, a pie chart of category-wise sales of electronic goods, and a line chart of month-wise total sales for the year 2020. 

![](https://github.com/fadialsalti/data_engineering_capstone_project/blob/main/all_files/dashboard.PNG)

To view the dashboard interactively on Cognos, visit the following link: https://eu-gb.dataplatform.cloud.ibm.com/dashboards/a0d06cf5-0f34-4e2f-8c26-5e05a797ccee/view/4f07c36439ea6fc355c1e2e407cb2e012c65215ae6bbd70a86837b495a677297a93d1492c82f4d5288150735fbbf110b9c

## Module 5
In this first part of the assignment, you will perform four exercises, but before proceeding with the assignment, you will prepare the lab environment by starting MySQL server, MongoDB server, and then downloading the files database from the given link. Further, you will import the data in the JSON file to a database and a collection, and the data in the SQL file to the MySQL server. You will also verify your access to the cloud instance of the IBM DB2 server. The first exercise requires you to extract the data from the sales tables in MySQL and from the MongoDB database into CSV format.

In the second exercise, you will transform the OLTP data to suit the data warehouse schema, read the OLTP data in the CSV format, add/edit/drop columns based on the data warehouse schema, and then save the transformed data into a new CSV file. In the third exercise, you will perform a series of tasks to transform the data. You will load the transformed data into the data warehouse, read the transformed data in the CSV format, load the transformed data into the data warehouse, and then, verify that the data is loaded properly. The final exercise requires you to automate the extraction of daily incremental data, and load yesterday's data into the data warehouse. You will download the python script from this link provided and use it as a template to write a python script that automatically loads yesterday's data from the production database into the data warehouse. After performing each task, take a screenshot of the command you used and its output, and name the screenshot.

Task 1 - Implement the function getlastrowid(): This function must connect to the DB2 data warehouse and return the last rowid.
```python
def get_last_rowid():
    SQL="SELECT MAX(rowid) FROM sales_data;"
    stmt = ibm_db.exec_immediate(conn, SQL)
    return ibm_db.fetch_tuple(stmt)[0]
```
Task 2 - Implement the function getlatestrecords(): This function must connect to the MySQL database and return all records later than the given last_rowid.
```python
def get_latest_records(rowid):
    SQL = "SELECT rowid FROM sales_data WHERE rowid > {};".format(last_row_id)
    cursor.execute(SQL)
    new_records = []
    for row in cursor.fetchall():
        new_records.append(row[0])
    return new_records
```
Task 3 - Implement the function insert_records(): This function must connect to the DB2 data warehouse and insert all the given records.
```python
def insert_records(records):
    SQL = "INSERT INTO sales_data (rowid,product_id,customer_id,quantity) VALUES(?,?,?,?);"
    to_insert = "SELECT * FROM sales_data WHERE rowid IN {};".format(tuple(new_records))
    cursor.execute(to_insert)
    for row in cursor.fetchall():
        stmt = ibm_db.prepare(conn, SQL)
        ibm_db.execute(stmt, row)
```
Task 4 - Test the data synchronization: Run the program automation.py and test if the synchronization is happening as expected.
![](https://github.com/fadialsalti/data_engineering_capstone_project/blob/main/all_files/synchronization.jpg)

The script is available in the repo as `automation.py`

--------------------------------------------------------------------------------------------------------------------------------
In this second part of the assignment, you will perform a couple of exercises, but before proceeding with the assignment, you will prepare the lab environment by starting the Apache Airflow and then downloading the dataset from the source (link provided) to the mentioned destination. In the first exercise, you will perform a series of tasks to create a DAG that runs daily. You will create a task that extracts the IP address field from the webserver log file and then saves it into a text file. The next task creation requires you to This task should filter out all the occurrences of ipaddress "198.46.149.143" from text file and save the output to a new text file. In the final task creation, you will load the data by archiving the transformed text file into a TAR file. Before moving on to the next exercise, you will define the task pipeline as per the given details.

In the second exercise, you will get the DAG operational by saving the defined DAG into a PY file. Further, you will submit, unpause and then monitor the DAG runs for the Airflow console. After performing each task, take a screenshot of the command you used and its output, and name the screenshot.

Task 1 - Define the DAG arguments.
```python
#defining DAG arguments
default_args = {
    'owner': 'Fadi Alsalti',
    'start_date': days_ago(0),
    'email': ['fadi.alsalti@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}
```
Task 2 - Define the DAG: Create a DAG named process_web_log that runs daily.
```python
# define the DAG
dag = DAG(
    dag_id='process_web_log',
    default_args=default_args,
    description='Apache Airflow Assignment for Module 5',
    schedule_interval=timedelta(days=1),
)
```
Task 3 - Create a task to extract data. This task should extract the ipaddress field from the web server log file and save it into a file named extracted_data.txt
```python
# define the first task named extract_data
extract_data = BashOperator(
    task_id='extract_data',
    bash_command='''wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/ETL/accesslog.txt;
    cut -d" " -f1 accesslog.txt > extracted_data.txt''',
    dag=dag,
)
```
Task 4 - Create a task to transform the data in the txt file. This task should filter out all the occurrences of ipaddress "198.46.149.143" from extracted_data.txt and save the output to a file named transformed_data.txt.
```python
# define the sixth task named transform_data
transform_data = BashOperator(
    task_id='transform_data',
    bash_command='grep -v 198.46.149.143 extracted_data.txt > transformed_data.txt',
    dag=dag,
)
```
Task 5 - Create a task to load the data. This task should archive the file transformed_data.txt into a tar file named weblog.tar.
```python
# define the sixth task named load_data
load_data = BashOperator(
    task_id='load_data',
    bash_command='tar -czvf weblog.tar transformed_data.txt',
    dag=dag,
)
```
Task 6 - Define the task pipeline.
```python
# task pipeline
extract_data >> transform_data >> load_data 
```
Task 7 - Submit the DAG.
```bash
cp process_web_log.py $AIRFLOW_HOME/dags
```
Task 8 - Unpause the DAG.
```bash
airflow dags unpause process_web_log
```
Task 9 - Monitor the DAG from Airflow console.
![](https://github.com/fadialsalti/data_engineering_capstone_project/blob/main/all_files/dag_runs.jpg)

The script is available in the repo as `process_web_log.py`

## Module 6
In this assignment, you will perform a number of tasks to analyse search terms on the e-commerce webserver. You will work in Watson Studio and within a Jupyter notebook to run your analysis against a CSV file containing the webserver data. You will load this file into a Spark dataframe and print the results of your queries against this dataset. You will then load a pretrained sales forecasting model and use this to predict the sales for 2023. After performing each task, take a screenshot of the code you used and its output, and name the screenshot.

The questions and answers of this last module are all detailed in the Jupyter Notebook `Spark_MLOps.ipynb` in the respository. 

------------------------------------------------------------------------------------
