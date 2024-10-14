SELECT p.product_name, 
       SUM(s.quantity) AS total_quantity
FROM {{ ref('transactions_seed') }} s
JOIN {{ ref('products_seed') }} p ON s.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_quantity DESC