import pyodbc
import pandas as pd
from tabulate import tabulate

conn = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=.;"
    "Database=TestDB;"
    "Trusted_Connection=yes;"
)
cursor = conn.cursor()

data = pd.read_csv(r"C:\Users\Agithui\Downloads\tickets.csv")
df = pd.DataFrame(data)

records = df.values.tolist()
sql_insert = """
         INSERT INTO tickets_table (Ticket_ID,Subject,Status,Priority,Source,Type,Agent,Group,created_time,
         due_by_time,resolved_time,Closed_time,Last_update_time,Initial_response_time,Time_tracked,
         First_response_time_in_hrs,Resolution_time_in_hrs,Agent_interactions,Customer_interactions,
         Resolution_status,First_response_status,Tags,Resolution_Priority,Assigned_To,Case_Type,
         Case_Category,Case_SubCategory,Source2,Escalated,Full_name,Contact_ID)
         VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
         """
cursor = conn.cursor()
cursor.executemany(sql_insert, records)
cursor.commit()
