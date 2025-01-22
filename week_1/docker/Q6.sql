SELECT tzldo."Zone", gt.tip_amount
 FROM green_tripdata as gt
 INNER JOIN taxi_zone_lookup AS tzl
 ON gt."PULocationID" = tzl."LocationID"
 INNER JOIN taxi_zone_lookup as tzldo
 on gt."DOLocationID" = tzldo."LocationID"
 WHERE tzl."Zone" = 'East Harlem North'
 ORDER BY 2 DESC
 LIMIT 1;