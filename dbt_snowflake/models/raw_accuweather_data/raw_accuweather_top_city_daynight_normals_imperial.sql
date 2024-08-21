SELECT
    *
FROM {{ source('accuweather_data','top_city_daynight_normals_imperial') }}