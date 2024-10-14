
  create view "think-thrift-db"."public"."products__dbt_tmp"
    
    
  as (
    SELECT *
FROM "think-thrift-db"."public"."products_seed"
  );