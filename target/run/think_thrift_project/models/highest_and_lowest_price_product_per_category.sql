
  create view "think-thrift-db"."public"."highest_and_lowest_price_product_per_category__dbt_tmp"
    
    
  as (
    SELECT 
product_name, category, price
FROM "think-thrift-db"."public"."products_seed"
WHERE price = (SELECT MAX(price) FROM products AS p WHERE p.category = products.category);
  );