import pyodbc
import pandas as pd
from tabulate import tabulate

conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=.;"
    "Database=TestDB;"
    "Trusted_Connection=yes;"
)
cursor = conn.cursor()

data = pd.read_csv(r"C:\Users\Agithui\Downloads\tickets.csv")
df = pd.DataFrame(data)

df = df.rename(columns={"Created time": "created_time"}, inplace=False)

# my_list = list(df)

# print(my_list)

for row in df.itertuples():
    cursor.execute(
        """
        INSERT INTO tickets_table (Subject,Status,Priority,Source,Type,Agent,Group,created_time,
        Due_by_Time,Resolved_time,Closed_time,Last_update_time,Initial_response_time,Time_tracked,
        First_response_time_in_hrs,Resolution_time_in_hrs,Agent_interactions,Customer_interactions,
        Resolution_status,First_response_status,Tags,Resolution_Priority,Assigned_To,Case_Type,
        Case_Category,Case_SubCategory,Source2,Escalated,Full_name,Contact_ID)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        """,
        row.Subject,
        row.Status,
        row.Priority,
        row.Source,
        row.Type,
        row.Agent,
        row.Group,
        row.created_time,
        row.Due_by_Time,
        row.Resolved_time,
        row.Closed_time,
        row.Last_update_time,
        row.Initial_response_time,
        row.Time_tracked,
        row.First_response_time_in_hrs,
        row.Resolution_time_in_hrs,
        row.Agent_interactions,
        row.Customer_interactions,
        row.Resolution_status,
        row.First_response_status,
        row.Tags,
        row.Resolution_Priority,
        row.Assigned_To,
        row.Case_Type,
        row.Case_Category,
        row.Case_SubCategory,
        row.Source2,
        row.Escalated,
        row.Full_name,
        row.Contact_ID,
    )

    conn.commit()
