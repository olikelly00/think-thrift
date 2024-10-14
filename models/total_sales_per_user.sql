SELECT 
  user_id, 
  SUM(quantity * price) AS total_sales
FROM {{ ref('transactions') }} 
JOIN {{ ref('products') }} 
ON transactions.product_id = products.product_id
GROUP BY user_id