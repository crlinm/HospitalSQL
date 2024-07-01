from psycopg2.extras import RealDictCursor


from config import (
    DB_HOST,
    DB_PORT,
    DB_NAME,
    DB_USER,
    DB_PASSWORD
)
import psycopg2
from pre_start import start_up
from workspace.base import start_workspace

# DB_USER = input("enter login, please: ")
# DB_PASSWORD = input("password: ")

conn = psycopg2.connect(
    database=DB_NAME,
    host=DB_HOST,
    port=DB_PORT,
    user=DB_USER,
    password=DB_PASSWORD
)

cur = conn.cursor(cursor_factory=RealDictCursor)


start_up(cur, conn)
start_workspace(cur, conn)
cur.close()
conn.close()
