import pandas as pd
import pyarrow.parquet as pq
import argparse
from sqlalchemy import create_engine
import os

# Connection parameters
def main():
    user = os.environ['POSTGRES_USER']
    password = os.environ['POSTGRES_PASSWORD']
    host = os.environ['POSTGRES_HOST']
    port = os.environ['POSTGRES_PORT']
    database = os.environ['POSTGRES_DATABASE']

    green_trip_data_file = "green_tripdata_2019-10.csv.gz"
    taxi_zone_lookup_file = "taxi_zone_lookup.csv"
    green_trip_table_name = "green_tripdata"
    taxi_zone_lookup_table_name = "taxi_zone_lookup"

    connection_string = f'postgresql://{user}:{password}@{host}:{port}/{database}'
    engine = create_engine(connection_string)

    # downloading the file
    os.system(f"wget https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-10.csv.gz -O {green_trip_data_file}")
    os.system(f"wget https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv -O {taxi_zone_lookup_file}")


    # Creating the tables in postgres
    green_trip_df = pd.read_csv(green_trip_data_file, compression='gzip')
    green_trip_df.head(n=0).to_sql(name=green_trip_table_name, con=engine, if_exists='replace')

    taxi_zone_lookup_df = pd.read_csv(taxi_zone_lookup_file)
    taxi_zone_lookup_df.head(n=0).to_sql(name=taxi_zone_lookup_table_name, con=engine, if_exists='replace')

    # Inserting the data into the table

    for chunk in pd.read_csv(green_trip_data_file, chunksize=10000, compression='gzip'):
        chunk.lpep_pickup_datetime = pd.to_datetime(chunk.lpep_pickup_datetime)
        chunk.lpep_dropoff_datetime = pd.to_datetime(chunk.lpep_dropoff_datetime)
        chunk.to_sql(name=green_trip_table_name, con=engine, if_exists='append')

    for chunk in pd.read_csv(taxi_zone_lookup_file, chunksize=10000):
        chunk.to_sql(name=taxi_zone_lookup_table_name, con=engine, if_exists='append')

if __name__ == '__main__':
    main()
