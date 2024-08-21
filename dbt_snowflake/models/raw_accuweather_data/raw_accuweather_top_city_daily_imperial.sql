SELECT
    *
FROM {{ source('accuweather_data','top_city_daily_imperial') }}