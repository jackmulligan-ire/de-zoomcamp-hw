SELECT tzl."Borough",tzl."Zone", sum(gt."total_amount")
 FROM green_tripdata as gt
 INNER JOIN taxi_zone_lookup AS tzl
 ON gt."PULocationID" = tzl."LocationID"
 WHERE 1 = 1
 and CAST(gt.lpep_pickup_datetime AS DATE) = '2019-10-18'
 group by 1,2 order by 3 desc limit 3;