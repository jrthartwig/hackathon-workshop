import os
import pyodbc
import json
from dotenv import load_dotenv
from openai import AzureOpenAI

# Load environment variables
load_dotenv()

# Set up Azure OpenAI client
client = AzureOpenAI(
    api_key=os.getenv("EMBEDDING_API_KEY"),
    api_version="2023-05-15",
    azure_endpoint=os.getenv("EMBEDDING_API_MODEL")
)

def generate_embeddings(text, model="text-embedding-ada-002"):
    return client.embeddings.create(input=[text], model=model).data[0].embedding

# SQL connection details
sql_connection_password = os.getenv("SQL_CONNECTION_PASSWORD")
driver = "{ODBC Driver 18 for SQL Server}"
server = os.getenv("SQL_SERVER")
database = os.getenv("SQL_DATABASE")
uid = os.getenv("SQL_UID")

full_sql_connection = f"Driver={driver};Server={server};Database={database};Uid={uid};Pwd={sql_connection_password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"

# Connect to Azure SQL
conn = pyodbc.connect(full_sql_connection)
cursor = conn.cursor()

# Add the Embedding column if it doesn't exist
try:
    cursor.execute("ALTER TABLE SalesLT.SalesOrderDetail ADD Embedding NVARCHAR(MAX);")
    conn.commit()
except pyodbc.ProgrammingError as e:
    if "Invalid column name 'Embedding'" not in str(e):
        raise

# Fetch data
cursor.execute("SELECT ProductID, OrderQty, UnitPrice, UnitPriceDiscount FROM SalesLT.SalesOrderDetail")
rows = cursor.fetchall()
print("fetched rows")

# Generate embeddings and store them in SQL
for row in rows:
    product_id, order_qty, unit_price, unit_price_discount = row
    input_text = f"{product_id} {order_qty} {unit_price} {unit_price_discount}"
    
    # Generate embedding
    embedding = generate_embeddings(input_text, model="text-embedding-ada-002")

    # Convert embedding to JSON string for storage
    embedding_json = json.dumps(embedding)

    # Store embeddings back in SQL
    cursor.execute("UPDATE SalesLT.SalesOrderDetail SET Embedding = ? WHERE ProductID = ?", (embedding_json, product_id))
    conn.commit()
    print("stored embeddings")

conn.close()