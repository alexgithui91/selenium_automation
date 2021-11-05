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
df = pd.DataFrame(
    data,
    columns=[
        "Ticket ID",
        "Subject",
        "Status",
        "Priority",
        "Source",
        "Type",
        "Agent",
        "Group",
        "Created time",
        "Due by Time",
        "Resolved time",
        "Closed time",
        "Last update time",
        "Initial response time",
        "Time tracked",
    ],
)

final_df = df.rename(columns={"Group": "ticket_group"})
final_df["Resolved time"].fillna("", inplace=True)
final_df["Closed time"].fillna("", inplace=True)
final_df["Initial response time"].fillna("", inplace=True)

final_df["Subject"] = final_df["Subject"].apply(str)
final_df["Type"] = final_df["Type"].apply(str)


records = final_df.values.tolist()

sql_insert = """
         INSERT INTO tickets_table (ticket_id,subject,status,priority,source,type,agent,ticket_group,
         created_time,due_by_time,resolved_time,closed_time,last_update_time,initial_response_time,time_tracked)
         VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
         """
cursor = conn.cursor()
cursor.executemany(sql_insert, records)
cursor.commit()
