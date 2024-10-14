import os
import pandas as pd
from lib.ingest_from_csv import ingest_and_clean_csv  

def test_ingest_from_csv():
    csv_file_path = os.path.join(os.path.dirname(__file__), '../seeds/users.csv')  # Adjust path as needed
    result = ingest_and_clean_csv(csv_file_path)
    
    assert result.iloc[0].to_dict() == {
        'user_id': 1,
        'username': 'JohnDoe',
        'country': 'US',
        'join_date': '2022-03-01',
        'email': 'johndoe@email.com',
        'user_rating': 4.5,
        'items_sold': 15,
        'items_bought': 5
    }
    
    assert result.iloc[9].to_dict() == {
        'user_id': 10,
        'username': 'LoisLane',
        'country': 'US',
        'join_date': '2022-12-25',
        'email': 'lois@email.com',
        'user_rating': 4.7,
        'items_sold': 18,
        'items_bought': 9
    }

def test_all_csv_data_is_ingested():
    csv_file_path = os.path.join(os.path.dirname(__file__), '../seeds/users.csv')  
    result = ingest_and_clean_csv(csv_file_path)
    print(result)
    
    assert len(result) == 10


def test_filter_products_by_category():
    csv_file_path = os.path.join(os.path.dirname(__file__), '../seeds/products.csv')
    result = ingest_and_clean_csv(csv_file_path)
    
    filtered_result = result[result['category'] == 'Accessories']
    
    assert len(filtered_result) == 3
    
    assert filtered_result.iloc[0]['product_name'] == 'Sunglasses'


def test_user_items_bought_matches_sales():
    users_csv_path = os.path.join(os.path.dirname(__file__), '../seeds/users.csv')
    sales_csv_path = os.path.join(os.path.dirname(__file__), '../seeds/transactions.csv')
    
    users = ingest_and_clean_csv(users_csv_path)
    sales = ingest_and_clean_csv(sales_csv_path)
    print("Users DataFrame:")
    print(users)
    print("\nSales DataFrame:")
    print(sales)
    
    sales_by_user = sales.groupby('user_id')['quantity'].sum().reset_index()
    print("\nSales grouped by user:")
    print(sales_by_user)
    
    merged_data = pd.merge(users, sales_by_user, how='inner', on='user_id')
    print("\nMerged Data:")
    print(merged_data)
    

    assert merged_data.iloc[0]['items_bought'] == merged_data.iloc[0]['quantity']
    assert merged_data.iloc[1]['items_bought'] == merged_data.iloc[1]['quantity']
    assert merged_data.iloc[8]['items_bought'] == merged_data.iloc[8]['quantity']
