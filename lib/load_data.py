import os
import pandas as pd
from lib.database_connection import DatabaseConnection
from lib.ingest_from_csv import ingest_and_clean_csv


# Load your DataFrame (users)
user_csv_file_path = os.path.join(os.path.dirname(__file__), '../seeds/users.csv')
products_csv_file_path = os.path.join(os.path.dirname(__file__), '../seeds/products.csv')
sales_csv_file_path = os.path.join(os.path.dirname(__file__), '../seeds/transactions.csv')


users = ingest_and_clean_csv(user_csv_file_path)
products = ingest_and_clean_csv(products_csv_file_path)
sales = ingest_and_clean_csv(sales_csv_file_path)


db = DatabaseConnection()
db.connect()

# Drop the tables if they exist
db.execute("DROP TABLE IF EXISTS sales;")


db.execute("DROP TABLE IF EXISTS transactions;")
db.execute("DROP TABLE IF EXISTS products;")
db.execute("DROP TABLE IF EXISTS users;")



# Create the table schema if it doesn't exist (example schema for users)
create_user_table_query = """
CREATE TABLE IF NOT EXISTS users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(100),
    country VARCHAR(50),
    join_date DATE,
    email VARCHAR(100),
    user_rating DECIMAL,
    items_sold INT,
    items_bought INT
);
"""

create_product_table_query = """
CREATE TABLE IF NOT EXISTS products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL,
    stock INT
);
"""

create_sales_table_query = """
CREATE TABLE IF NOT EXISTS transactions (
    transaction_id SERIAL PRIMARY KEY,
    user_id INT,
    product_id INT,
    sale_date DATE,
    quantity INT,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
"""


db.execute(create_user_table_query)
db.execute(create_product_table_query)
db.execute(create_sales_table_query)

# Insert data row by row into the PostgreSQL table
for index, row in users.iterrows():
    user_insert_query = """
    INSERT INTO users (username, country, join_date, email, user_rating, items_sold, items_bought)
    VALUES (%s, %s, %s, %s, %s, %s, %s);
    """
    db.execute(user_insert_query, [row['username'], row['country'], row['join_date'], row['email'], row['user_rating'], row['items_sold'], row['items_bought']])

print("Users inserted successfully!")

for index, row in products.iterrows():
    product_insert_query = """
    INSERT INTO products (product_name, category, price)
    VALUES (%s, %s, %s);
    """
    db.execute(product_insert_query, [row['product_name'], row['category'], row['price']])

print("Products inserted successfully!")

for index, row in sales.iterrows():
    sales_insert_query = """
    INSERT INTO transactions (user_id, product_id, sale_date, quantity)
    VALUES (%s, %s, %s, %s);
    """
    db.execute(sales_insert_query, [row['user_id'], row['product_id'], row['sale_date'], row['quantity']])

print("Sales inserted successfully!")

print(db.execute("SELECT * FROM transactions"))
print(db.execute("SELECT * FROM products"))
print(db.execute("SELECT * FROM users"))

