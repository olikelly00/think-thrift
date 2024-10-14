SELECT 
product_name, category, price
FROM "think-thrift-db"."public"."products"
WHERE price = (SELECT MAX(price) FROM products AS p WHERE p.category = products.category)