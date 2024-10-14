
  create view "think-thrift-db"."public"."total_sales_per_user__dbt_tmp"
    
    
  as (
    SELECT 
  user_id, 
  SUM(quantity * price) AS total_sales
FROM "think-thrift-db"."public"."transactions" 
JOIN "think-thrift-db"."public"."products" 
ON transactions.product_id = products.product_id
GROUP BY user_id
  );