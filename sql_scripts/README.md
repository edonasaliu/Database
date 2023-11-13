# Health and Fitness Tracking App - SQL Scripts

## Overview

This document provides an overview and instructions for the SQL scripts used in the Health and Fitness Tracking App. These scripts are designed to create the database schema, insert data, and run various queries for the application.

## Files Description

- `create_tables.sql`: This script contains SQL commands to create all the necessary tables for the Health and Fitness Tracking App. It includes tables for users, workouts, exercises, nutrition logs, meals, sleep records, and health metrics.

- `insert_data.sql`: This script is used to insert sample data into the tables. It helps in testing and demonstrating how the database works with actual data.

- `query_data.sql`: Contains various SQL queries to extract meaningful information from the database. These queries demonstrate how the app can retrieve data for user insights, workout analysis, nutrition tracking, etc.

## How to Use

### Setting Up the Database

1. **Open SQLite Command Line Tool**: Navigate to your project directory in the terminal or command prompt and open SQLite command line tool by running `sqlite3`.

2. **Connect to Your Database**: Connect to your SQLite database by running:

   ```bash
   sqlite3 HealthAndFitnessApp.db

3. **Create Tables**: Run the create_tables.sql script to set up your database schema:
    ```sqlite3
    .read create_tables.sql
    

## Populating the Database

1. **Insert Data**: After creating the tables, use the insert_data.sql script to populate the database with sample data:
    ```sqlite3
    .read insert_data.sql


## Running Queries

1. **Execute Queries**: Use the query_data.sql script to run predefined queries:
    ```sqlite3
    .read query_data.sql


### Notes
- Ensure that SQLite is installed and properly set up on your machine.