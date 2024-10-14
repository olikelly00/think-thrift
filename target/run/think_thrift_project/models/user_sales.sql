
  create view "think-thrift-db"."public"."user_sales__dbt_tmp"
    
    
  as (
    SELECT u.username, 
       SUM(s.quantity * p.price) AS total_sales
FROM "think-thrift-db"."public"."transactions_seed" s
JOIN "think-thrift-db"."public"."users_seed" u ON s.user_id = u.user_id
JOIN "think-thrift-db"."public"."products_seed" p ON s.product_id = p.product_id
GROUP BY u.username
  );