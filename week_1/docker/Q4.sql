SELECT lpep_pickup_datetime 
FROM green_tripdata
WHERE 1 = 1
AND trip_distance = (select max(trip_distance) from green_tripdata);