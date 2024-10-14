
  create view "think-thrift-db"."public"."users_since_2022__dbt_tmp"
    
    
  as (
    SELECT * 
FROM "think-thrift-db"."public"."users"
WHERE join_date >= '2022-01-01'
  );