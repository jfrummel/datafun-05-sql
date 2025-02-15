import sqlite3
import pathlib
import pandas as pd
import matplotlib.pyplot as plt

# Define paths to database and SQL queries
db_file_path = pathlib.Path("data/db.sqlite")
queries_folder = pathlib.Path("sql_queries")

# Function to execute a single SQL query and return the result as a DataFrame
def execute_sql_query(db_file_path, sql_query):
    try:
        with sqlite3.connect(db_file_path) as conn:
            # Execute query and check if there are results
            df = pd.read_sql_query(sql_query, conn)
            
            return df
    except sqlite3.Error as e:
        print(f"Error executing query: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

# Function to read and split queries in the SQL file
def read_sql_file(sql_file_path):
    try:
        if not sql_file_path.exists():
            print(f"Error: The SQL file '{sql_file_path}' does not exist.")
            return []
        with open(sql_file_path, "r") as file:
            sql_query = file.read().strip()
            # Split the queries based on the semicolon delimiter
            queries = [query.strip() for query in sql_query.split(';') if query.strip()]
            return queries
    except Exception as e:
        print(f"Error reading SQL file {sql_file_path}: {e}")
        return []

# Function to plot the results of a query (for aggregation and grouping)
def plot_join_results(df, title):
        df.plot(kind='bar', x=df.columns[0], y=df.columns[1:], legend=True)
        plt.title(title)
        plt.xlabel(df.columns[0])
        plt.ylabel('Count')
        plt.show()


# Function to execute and display the query results
def run_queries():
    # Run aggregation query
    aggregation_queries = read_sql_file(queries_folder.joinpath("query_aggregation.sql"))
    for query in aggregation_queries:
        aggregate_df = execute_sql_query(db_file_path, query)
        print(f'Aggregation Results: \n{aggregate_df}')

    # Run filtering query
    filtering_queries = read_sql_file(queries_folder.joinpath("query_filter.sql"))
    for query in filtering_queries:
        filter_df = execute_sql_query(db_file_path, query)
        print(f'Filtered Results: \n{filter_df}')

    # Run sorting query
    sorting_queries = read_sql_file(queries_folder.joinpath("query_sorting.sql"))
    for query in sorting_queries:
        sort_df = execute_sql_query(db_file_path, query)
        print(f'Sorted Results: \n{sort_df}')

    # Run grouping query
    grouping_queries = read_sql_file(queries_folder.joinpath("query_group_by.sql"))
    for query in grouping_queries:
        group_df = execute_sql_query(db_file_path, query)
        print(f'Group By Results: \n{group_df}')
            

    # Run join query
    joining_queries = read_sql_file(queries_folder.joinpath("query_join.sql"))
    for query in joining_queries:
        join_df = execute_sql_query(db_file_path, query)
        print(f'Join Results: \n{join_df}')
        plt.bar(join_df["name"], join_df["goals"])
        plt.xlabel("Player")
        plt.ylabel("Goals")
        plt.title("Goals by Player")
        plt.show()
    



def main():
    run_queries()

if __name__ == "__main__":
    main()