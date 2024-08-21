SELECT
    *
FROM {{ source('accuweather_data','top_city_hourly_metric') }}