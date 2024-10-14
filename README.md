# ♻️👕 ThinkThrift: Data Engineering Workflows 👕♻️

**ThinkThrift** is a community-powered, peer-to-peer platform designed for the resale of second-hand clothing. To support that mission, teams across marketing, sales, product, and engineering rely on reliable, well-structured data to drive business and product decisions.

## Project Overview

This project focuses on building the **data engineering workflows** that empower these teams to scale ThinkThrift and enhance its impact. I have implemented a combination of Python, Pytest, pandas, and PostgreSQL to create efficient, well-tested pipelines for extracting, transforming, and loading CSV data.

In addition to data ingestion, I have used SQL and dbt to build model views—predefined SQL commands that join multiple database tables to provide relevant data sets for various team needs. By incorporating Jinja syntax, I’ve parameterized queries, making them dynamic so that users can pass their own search terms and generate custom data sets.

Future plans include integrating Looker to offer data insights through a user-friendly dashboard, and using Fivetran to automate the process of syncing ThinkThrift’s Postgres database with external tools like Looker.

More details on the achievements, challenges, and future plans for Data Engineering at ThinkThrift are outlined below.


## Achievements So Far

-   **Data Pipeline Setup**:

    -   **PostgreSQL** database called think-thrift-db serves as the database for storing Think-Thrift's critical data, including user data, product details and transaction history.


-   **Data Ingestion with Pandas** 🐼:

    -   Ingested initial datasets into PostgreSQL using **pandas**, enabling clean and structured data loading. This step supports efficient querying and dbt transformations, reducing manual data handling.

- **What do I mean by 'cleaning' the data using Pandas?**:

    - Stripping Whitespace from Column Names: this ensures that column names are consistent and error-free, preventing issues when referencing columns later. Inconsistent column names can lead to errors or difficulty in accessing data
    
    - Filling Missing Values: missing values can cause errors or make data analysis inaccurate. By filling them with a default value like "Unknown," we maintain data integrity and prevent processing interruptions.
    
    - Converting Columns to Numeric: ensures that columns with numeric data (e.g., quantities, prices) are in the correct format for calculations or aggregations. This helps avoid errors in further analysis or reporting.
    
    - Removing Duplicates: duplicate data can skew results or overstate certain metrics. By removing them, the dataset remains clean and representative of actual transactions or user behavior.


-   **dbt for Data Transformations**:

    -   **dbt (Data Build Tool)** has been incorporated to manage data transformations and implement **modular SQL models**. These models optimise the pipeline by structuring the data in a way that improves query performance and allows for dynamic querying.

   
-   **Security & SSL Configuration**:

    -   Configured **SSL** for PostgreSQL to ensure secure data communication. Updated the PostgreSQL configuration to point to the appropriate SSL certificate and key, following best practices for data protection.

	⁃	**Dynamic SQL queries using Jinja ☕️**

    -   **Jinja templating** in dbt is used to make queries flexible by incorporating variables and filters. This allows for scalable data models that are adaptable to new user data and categories.

-   **Real-Time Data Replication**:

    -   Configured **logical replication** on PostgreSQL by setting up WAL (Write-Ahead Logging) and creating replication slots (my_slot) and a publication (my_publication), ensuring continuous, real-time syncing of the database.


## Work-in-progress

-   **Fivetran Integration**: 
    
    - The aim is to use Fivetran to automate the process of syncing Think-Thrift's Postgres database with external tools, including analytics platforms such as **Looker**. I'm keen to set this up because it simplifies the process of building self-serve analytics for users, helping ThinkThrift's employees get the data they need easily and quickly.

-   **Looker Integration**:

    -   Initially aimed to connect PostgreSQL with **Looker** to create a dashboard for easily accessible data insights. Challenges around secure connection management led to the use of **Fivetran** to simplify and automate the integration with Looker.



## Tools and Technologies

-   **PostgreSQL**: The database used for storing user, product, and transaction data.

-   **dbt**: Managing data transformations and creating dynamic queries with Jinja templating for scalable, modular SQL models.

-   **pandas**: Used for ingesting and pre-processing CSV data before it enters the PostgreSQL database.

-   **Fivetran**: Automates real-time data replication from PostgreSQL to Looker, making the integration with analytics platforms simpler and more seamless.

-   **SSL**: Ensures secure communication between the database and external services such as Fivetran.