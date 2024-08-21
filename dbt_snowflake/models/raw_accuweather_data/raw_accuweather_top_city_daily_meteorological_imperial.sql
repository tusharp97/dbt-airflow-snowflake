SELECT
    *
FROM {{ source('accuweather_data','top_city_daily_meteorological_imperial') }}