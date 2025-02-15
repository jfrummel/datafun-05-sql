# datafun-05-sql

#Project 5 SQL Module

## Overview

This project utitlizes SQL and Python in the creation and manipulation of a database.

---

## Step 1: Create a repo in Github and clone locally.


1. `git clone <github repo url>` 
2. Add .gitignore, README.md and requirements.txt


---

## Step 2: Create and activate virtual environment

1. `py -m venv .venv`
2. `.venv\Scripts\activate`



## Step 3: Install Dependencies
1. `py -m pip install --upgrade pip setuptools wheel`
2. `py -m pip install -r requirements.txt`


## Step 4: Add, commit and push changes to Github




## Step 5: Schema Design and Database Initialization

1.  Create sql_create folder 
    - 01_drop_tables.sql - drop tables to restart
    - 02_create_tables.sql - create your database schema using sql 
    - 03_insert_records.sql - insert at least 10 additional records into each table.



2. Create db01_setup.py:
    Using the sql_create folder, this file creates and inserts records into table.




## Step 6: Cleaning and Feature Engineering

1. Create a sql_features folder 
   - update_records.sql - upates a record
   - delete_records.sql - deletes records
2. Created db02_features.py file - script that runs the update and delete scripts
 


## Step 7. Perform Aggregations and queries

1. Create an sql_queries folder which includes:
   - query_aggregation.sql - use aggregation functions including COUNT, AVG, SUM.
   - query_filter.sql - use WHERE to filter data based on conditions.
   - query_sorting.sql - use ORDER BY to sort data.
   - query_group_by.sql - use GROUP BY clause (and optionally with aggregation)
   - query_join.sql - use INNER JOIN operation and optionally include LEFT JOIN, RIGHT JOIN, etc.
2. Create db03_queries.py which will run the queries
