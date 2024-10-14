
  create view "think-thrift-db"."public"."users__dbt_tmp"
    
    
  as (
    SELECT *
FROM "think-thrift-db"."public"."users_seed"
  );