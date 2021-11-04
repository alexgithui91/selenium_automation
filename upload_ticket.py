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

df = df.rename(
    columns={
        "Created time": "created_time",
        "Due by Time": "due_by_time",
        "Resolved time": "resolved_time",
        "Closed time": "closed_time",
        "Last update time": "last_update_time",
        "Initial response time": "initial_response_time",
        "Time tracked": "time_tracked",
        "First response time (in hrs)": "first_response_time",
        "Resolution time (in hrs)": "resolution_time",
        "Agent interactions": "agent_interactions",
        "Customer interactions": "customer_interactions",
        "Resolution status": "resolution_status",
        "First response status": "first_response_status",
        "Resolution Priority": "resolution_priority",
        "Assigned To": "assigned_to",
        "Case Type": "case_type",
        "Case Category": "case_category",
        "Case SubCategory": "case_subcategory",
        "Source.1": "source2",
        "Full name": "full_name",
        "Contact ID": "contact_id",
    },
    inplace=False,
)

# my_list = list(df)

# print(my_list)

for row in df.itertuples():
    cursor.execute(
        """
        INSERT INTO tickets_table (Subject,Status,Priority,Source,Type,Agent,Group,created_time,
        due_by_time,resolved_time,Closed_time,Last_update_time,Initial_response_time,Time_tracked,
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
        row.due_by_time,
        row.resolved_time,
        row.closed_time,
        row.last_update_time,
        row.initial_response_time,
        row.time_tracked,
        row.first_response_time,
        row.resolution_time,
        row.agent_interactions,
        row.customer_interactions,
        row.resolution_status,
        row.first_response_status,
        row.Tags,
        row.resolution_priority,
        row.assigned_to,
        row.case_type,
        row.case_category,
        row.case_subcategory,
        row.source2,
        row.Escalated,
        row.full_name,
        row.contact_id,
    )

    conn.commit()
