import os
import json
import requests
import pyodbc
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up Azure OpenAI client details
api_key = os.getenv("OPEN_AI_API_KEY")
api_version = "2023-03-15-preview"
azureopenai_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
model = "4o"

# SQL connection details
sql_connection_password = os.getenv("SQL_CONNECTION_PASSWORD")
driver = "{ODBC Driver 18 for SQL Server}"
full_sql_connection = f"Driver={driver};Server=tcp:destinationvahackathon.database.windows.net,1433;Database=sourcedatabase_Copy;Uid=vahackathon;Pwd={sql_connection_password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30"

def fetch_embeddings():
    conn = pyodbc.connect(full_sql_connection)
    cursor = conn.cursor()
    cursor.execute("SELECT ProductID, OrderQty, UnitPrice, UnitPriceDiscount, Embedding FROM SalesLT.SalesOrderDetail")
    rows = cursor.fetchall()
    conn.close()
    return rows

def chat_with_data(question, products):
    url = f"{azureopenai_endpoint}/openai/deployments/{model}/chat/completions?api-version={api_version}"
    headers = {
        "Content-Type": "application/json",
        "api-key": api_key 
    }
    system_message = {
    "role": "system",
    "content": (
        "You are a system assistant who helps detect anomalies in product data. "
        "Products will be provided in an assistant message in the format of 'Id=>Product=>OrderQty=>UnitPrice=>UnitPriceDiscount'. "
        "You can use this information to help you answer the user's question about potential anomalies in the data."
        )
    }
    user_message = {
        "role": "user",
        "content": f"## Source ##\n{products}\n## End ##\n\nYour answer needs to be a JSON object with the following format:\n"
                "{\n"
                "    \"answer\": // the answer to the question, add a source reference to the end of each sentence. Source reference is the product Id.\n"
                "    \"products\": // a comma-separated list of product ids that you used to come up with the answer.\n"
                "    \"thoughts\": // brief thoughts on how you came up with the answer, e.g., what sources you used, what you thought about, etc.\n"
                "}"
    }

    question_message = {
        "role": "user",
        "content": question
    }
    payload = json.dumps({
        "messages": [system_message, user_message, question_message],
        "max_tokens": 800,
        "temperature": 0.7,
        "frequency_penalty": 0,
        "presence_penalty": 0,
        "top_p": 0.95,
        "stop": None
    })
    response = requests.post(url, headers=headers, data=payload)
    response.raise_for_status()
    return response.json()

# Fetch embeddings from SQL
rows = fetch_embeddings()

# Format the product data
products = "\n".join([f"{row.ProductID}=>{row.OrderQty}=>{row.UnitPrice}=>{row.UnitPriceDiscount}" for row in rows])

# Example question
question = "Do you see any trends or anomalies in the product data?"

try:
    # Generate response
    response = chat_with_data(question, products)
    print("Generated response:", response)
except requests.exceptions.RequestException as e:
    print("Error during API call:", e)
