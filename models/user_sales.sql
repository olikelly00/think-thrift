SELECT u.username, 
       SUM(s.quantity * p.price) AS total_sales
FROM {{ ref('transactions_seed') }} s
JOIN {{ ref('users_seed') }} u ON s.user_id = u.user_id
JOIN {{ ref('products_seed') }} p ON s.product_id = p.product_id
GROUP BY u.username