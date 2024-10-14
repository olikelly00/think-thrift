SELECT * 
FROM {{ ref('users') }}
WHERE join_date >= '{{ var('join_date', '2022-01-01') }}'