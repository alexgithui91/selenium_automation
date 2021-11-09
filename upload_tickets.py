import pyodbc
import pandas as pd

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
        "First response time (in hrs)",
        "Resolution time (in hrs)",
        "Agent interactions",
        "Customer interactions",
        "Resolution status",
        "First response status",
        "Tags",
        "Resolution Priority",
        "Assigned To",
        "Case Type",
        "Case Category",
        "Case SubCategory",
        "Escalated",
        "Full name",
        "Contact ID",
    ],
)

final_df = df.rename(columns={"Group": "ticket_group"})
final_df["Resolved time"].fillna("", inplace=True)
final_df["Closed time"].fillna("", inplace=True)
final_df["Initial response time"].fillna("", inplace=True)
final_df["Resolution status"].fillna("", inplace=True)
final_df["First response status"].fillna("", inplace=True)
final_df["Tags"].fillna("", inplace=True)
final_df["Resolution Priority"].fillna("", inplace=True)
final_df["Assigned To"].fillna("", inplace=True)
final_df["Case Type"].fillna("", inplace=True)
final_df["Case Category"].fillna("", inplace=True)
final_df["Case SubCategory"].fillna("", inplace=True)

final_df["Subject"] = final_df["Subject"].apply(str)
final_df["Type"] = final_df["Type"].apply(str)

records = final_df.values.tolist()

sql_insert = """
         INSERT INTO tickets_table (ticket_id,subject,status,priority,source,type,agent,ticket_group,
         created_time,due_by_time,resolved_time,closed_time,last_update_time,initial_response_time,
         time_tracked,first_response_time_in_hrs,resolution_time_in_hrs,agent_interactions,customer_interactions,
         resolution_status,first_response_status,tags,resolution_priority,assigned_to,case_type,case_category,
         case_subcategory,escalated,full_name,contact_id)
         VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
         """
cursor = conn.cursor()
cursor.executemany(sql_insert, records)
cursor.commit()
