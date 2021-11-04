import pyodbc
import pandas as pd

conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=.;"
    "Database=TestDB;"
    "Trusted_Connection=yes;"
)
cursor = conn.cursor()
