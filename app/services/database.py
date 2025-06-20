import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()

def get_client_info(phone):
    conn = pyodbc.connect(
        f"DRIVER={{{os.getenv('MSSQL_DB_DRIVER')}}};"
        f"SERVER={os.getenv('MSSQL_DB_HOST')},{os.getenv('MSSQL_DB_PORT')};"
        f"DATABASE={os.getenv('MSSQL_DATABASE_NAME')};"
        f"UID={os.getenv('MSSQL_DB_USERNAME')};"
        f"PWD={os.getenv('MSSQL_DB_PASSWORD')}"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT TOP 1 CustNo, CName, MobTel FROM dbo.ResCustInfo WHERE MobTel LIKE ?", f"%{phone}%")
    row = cursor.fetchone()
    conn.close()
    if row:
        return dict(zip([column[0] for column in cursor.description], row))
    return None
