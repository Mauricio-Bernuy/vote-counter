
import functions_framework
from google.cloud import storage
import sqlalchemy
# import pandas as pd
# import base64
# import json
# import os

connection_name = "evident-ratio-307301:southamerica-east1:votes-db"
table_name = "votos"
db_name = "postgres"
db_user = "postgres"
db_password = "pogaso"

driver_name = 'postgres+pg8000'
query_string =  dict({"unix_sock": "/cloudsql/{}/.s.PGSQL.5432".format(connection_name)})


# Triggered by a change in a storage bucket
@functions_framework.cloud_event
def hello_gcs(cloud_event):
    
    db = sqlalchemy.create_engine(
      sqlalchemy.engine.url.URL(
        drivername=driver_name,
        username=db_user,
        password=db_password,
        database=db_name,
        query=query_string,
      ),
      pool_size=5,
      max_overflow=2,
      pool_timeout=30,
      pool_recycle=1800
    )

    stmt = sqlalchemy.text('SELECT 1;')
    print("in CF!!")  
    print("before connect")
    with db.connect() as conn:
      print("after connect")
      conn.execute(stmt)
      print("after execute")
    return 'ok'

   data = cloud_event.data
   bucket_name = data["bucket"]
   blob_name = data["name"]
   print("retreiving file from:", bucket_name, blob_name)

   storage_client = storage.Client()
   bucket = storage_client.bucket(bucket_name)
   blob = bucket.blob(blob_name)

   data_bytes = blob.download_as_bytes()
   print("file as bytes done")
   df = pd.read_excel(data_bytes)
   print("excel shape:", df.shape)
   
   df.to_sql(table_name, db, if_exists='append', chunksize=1000)

  #  ///////////////////////////

# This file contains all the code used in the codelab. 
import sqlalchemy

# Depending on which database you are using, you'll set some variables differently. 
# In this code we are inserting only one field with one value. 
# Feel free to change the insert statement as needed for your own table's requirements.

# Uncomment and set the following variables depending on your specific instance and database:
connection_name = "evident-ratio-307301:southamerica-east1:votes-db"
table_name = "votos"
#table_field = ""
#table_field_value = ""
db_name = "postgres"
db_user = "postgres"
db_password = "pogaso"

# If your database is MySQL, uncomment the following two lines:
#driver_name = 'mysql+pymysql'
#query_string = dict({"unix_socket": "/cloudsql/{}".format(connection_name)})

# If your database is PostgreSQL, uncomment the following two lines:
driver_name = 'postgres+pg8000'
query_string =  dict({"unix_sock": "/cloudsql/{}/.s.PGSQL.5432".format(connection_name)})

# If the type of your table_field value is a string, surround it with double quotes.

@functions_framework.cloud_event
def hello_gcs(cloud_event):
    # request_json = request.get_json()
    stmt = sqlalchemy.text('select 1')
    
    db = sqlalchemy.create_engine(
      sqlalchemy.engine.url.URL(
        drivername=driver_name,
        username=db_user,
        password=db_password,
        database=db_name,
        query=query_string,
      ),
      pool_size=5,
      max_overflow=2,
      pool_timeout=30,
      pool_recycle=1800
    )
    # try:
    print("before connect")
    with db.connect() as conn:
      print("after connect")
      conn.execute(stmt)
      print("after execute")
    # except Exception as e:
        # return 'Error: {}'.format(str(e))
    return 'ok'