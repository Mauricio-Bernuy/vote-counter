import functions_framework
from google.cloud.sql.connector import Connector
import sqlalchemy


# Triggered by a change in a storage bucket
@functions_framework.cloud_event
def hello_gcs(cloud_event):

  project_id = "evident-ratio-307301"
  region = "southamerica-east1"
  instance_name = "votes-db"
  INSTANCE_CONNECTION_NAME = f"{project_id}:{region}:{instance_name}" # i.e demo-project:us-central1:demo-instance
  DB_USER = "postgres"
  DB_PASS = "pogaso"
  DB_NAME = "postgres"
  print(f"Your instance connection name is: {INSTANCE_CONNECTION_NAME}")

  connector = Connector()
  def getconn():
    conn = connector.connect(
      INSTANCE_CONNECTION_NAME,
      "pg8000",
      user=DB_USER,
      password=DB_PASS,
      db=DB_NAME
    )
    return conn

  pool = sqlalchemy.create_engine(
      "postgresql+pg8000://",
      creator=getconn,
  )

  with pool.connect() as db_conn:
    results = db_conn.execute("SELECT * FROM votos").fetchall()
    print("fetched results!")
    # show results
    for row in results:
      print(row)