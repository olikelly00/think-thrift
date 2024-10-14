
  create view "think-thrift-db"."public"."transactions__dbt_tmp"
    
    
  as (
    SELECT *
FROM "think-thrift-db"."public"."transactions_seed"
  );