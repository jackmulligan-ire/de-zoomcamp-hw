WITH mile_buckets AS (
    SELECT
    CASE
        WHEN trip_distance <= 1 THEN 'Up to 1 mile'
        WHEN trip_distance > 1 AND trip_distance <= 3 THEN '1 to 3 miles'
        WHEN trip_distance > 3 AND trip_distance <= 7 THEN '3 to 7 miles' 
        WHEN trip_distance > 7 AND trip_distance <= 10 THEN '7 to 10 miles'
        ELSE 'Over 10 miles'
    END AS DISTANCE_BUCKET
    FROM green_tripdata
) 
SELECT DISTANCE_BUCKET, count(*) FROM mile_buckets GROUP BY 1 ORDER BY 1;