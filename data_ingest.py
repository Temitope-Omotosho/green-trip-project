import pandas as pd
#import wget
from sqlalchemy import create_engine

data_list = []
for i in range(1,13):
    if i < 10:
        data_list.append(pd.read_parquet('green_tripdata_2022-0{}.parquet'.format(i)))
    else:
        data_list.append(pd.read_parquet('green_tripdata_2022-{}.parquet'.format(i)))


trip_data = pd.concat(data_list,axis=0,ignore_index=True)
print(trip_data)
##