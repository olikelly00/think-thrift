from lib.load_data import load_data
from lib.database_connection import DatabaseConnection


def test_total_sales_by_user():
    db = DatabaseConnection()
    db.connect()
    
    query = """
    SELECT u.username, SUM(s.quantity * p.price) AS total_sales
    FROM transactions s
    JOIN users u ON s.user_id = u.user_id
    JOIN products p ON s.product_id = p.product_id
    GROUP BY u.username;
    """
    
    result = db.execute(query)
    
    expected_result = [
        {"username": "JohnDoe", "total_sales": 40.00},
        {"username": "JaneSmith", "total_sales": 50.00}
    ]
    
    result_list = [{"username": row['username'], "total_sales": float(row['total_sales'])} for row in result]
    
    assert result_list == expected_result, f"Expected {expected_result}, but got {result_list}"
