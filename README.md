# Product Anomaly Detection Lab

This lab will guide you through setting up Azure SQL servers, seeding data, generating embeddings using Azure OpenAI, and using Retrieval Augmented Generation (RAG) to detect anomalies in product data.

Reference Documentation: 
* [Azure SQL General Documentation](https://learn.microsoft.com/en-us/azure/azure-sql/database/sql-database-paas-overview?view=azuresql)
* [Azure OpenAI General Documentation](https://learn.microsoft.com/en-us/azure/ai-services/openai/overview)
* [Azure OpenAI Python Reference](https://learn.microsoft.com/en-us/azure/ai-services/openai/references/on-your-data?tabs=python#tabpanel_1_python)
* [Pyodbc](https://learn.microsoft.com/en-us/sql/connect/python/pyodbc/step-3-proof-of-concept-connecting-to-sql-using-pyodbc?view=sql-server-ver16)
* [RAG](https://learn.microsoft.com/en-us/azure/ai-studio/concepts/retrieval-augmented-generation)

## 1. Creating a Source SQL Server and Seeding Data

### Step 1: Create a Source SQL Server
1. Log in to portal.azure.com.
2. Create a resource group and add an Azure SQL Server.
3. Fill in the required details to create a new SQL server and database.
4. Select the option to add AdventureWorks data.
5. Once created, navigate to the SQL server and select **Networking**.
6. Allow **Selected networks** and add your client IP address to the firewall rules.

## 2. Creating a Destination SQL Server

### Step 1: Create a Destination SQL Server
1. Repeat the steps from **Creating a Source SQL Server** to create another SQL server and database. This will be your destination SQL server.

## 3. Creating an Azure OpenAI Instance

### Step 1: Create an Azure OpenAI Resource
1. Log in to portal.azure.com.
2. Navigate to **Create a resource** and search for **Azure OpenAI**.
3. Click **Create** and fill in the required details to create an Azure OpenAI resource.
4. Once created, navigate to the resource and note down the **Endpoint** and **API Key**. These will be used in your `.env` file.

### Step 2: Deploy a GPT-4o Model
1. In your Azure OpenAI resource, navigate to **Deployments**.
2. Click **+ Create** to create a new deployment.
3. Select the GPT-4o model from the list of available models.
4. Fill in the required details and click **Create** to deploy the model.
5. Note down the deployment name, as it will be used in your scripts.

## 4. Copying Data from Source to Destination

### Step 1: Copy Data Using Azure Portal
1. Navigate to your source SQL database.
2. Select **Copy** from the toolbar.
3. Fill in the required details to copy the database to your destination SQL server.
4. Confirm the copy operation.

### Step 2: Verify Data Copy
1. Navigate to your destination SQL database.
2. Open the **Query editor** and run a simple query to confirm the data has been copied:
    ```sql
    SELECT TOP 10 * FROM SalesLT.SalesOrderDetail;
    ```

## 5. Setup

### Step 1: Install Python and ODBC Driver for Windows
1. Download and install Python from [Python Downloads](https://www.python.org/downloads/).
2. Download and install ODBC Driver for Windows [ODBC Driver](https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver16).

### Step 2: Clone the Repository
1. Open a terminal and run the following commands:
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

### Step 3: Set Up a Virtual Environment
1. Create a virtual environment:
    ```bash
    python -m venv venv
    ```
2. Activate the virtual environment:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

### Step 4: Install Required Packages
1. Install the required packages using `pip`:
    ```bash
    pip install -r requirements.txt
    ```

### Step 5: Set Up Environment Variables
1. Create a `.env` file in the root directory of the project.
2. Copy the contents of `example.env` to `.env` and fill in your own values:
    ```plaintext
    OPEN_AI_API_KEY=your_openai_api_key
    AZURE_OPENAI_ENDPOINT=https://your_azure_openai_endpoint
    EMBEDDING_API_KEY=your_embedding_api_key
    EMBEDDING_API_MODEL=https://your_embedding_api_model
    SQL_CONNECTION_PASSWORD=your_sql_connection_password
    ```

## 6. Add Embeddings Python Script

### Steps in `add-embeddings.py`
1. **Load Environment Variables**: The script loads environment variables from the `.env` file.
2. **Set Up Azure OpenAI Client**: Initializes the Azure OpenAI client using the API key and endpoint.
3. **Connect to Azure SQL**: Establishes a connection to the destination SQL database.
4. **Add Embedding Column**: Adds an `Embedding` column to the `SalesLT.SalesOrderDetail` table if it doesn't exist.
5. **Fetch Data**: Retrieves product data from the SQL database.
6. **Generate Embeddings**: Uses Azure OpenAI to generate embeddings for each product data row.
7. **Store Embeddings**: Stores the generated embeddings back in the SQL database.

## 7. Query Embeddings in Azure Query Editor

### Step 1: Query Embeddings
1. Navigate to your destination SQL database in the Azure Portal.
2. Open the **Query editor** and run a query to view the embeddings:
    ```sql
    SELECT TOP 10 ProductID, Embedding FROM SalesLT.SalesOrderDetail;
    ```

## 8. Chat with Data Python Script

### Steps in `chat-with-data.py`
1. **Load Environment Variables**: The script loads environment variables from the `.env` file.
2. **Fetch Embeddings**: Connects to the SQL database and retrieves the embeddings.
3. **Format Product Data**: Formats the product data for input into the Azure OpenAI model.
4. **Generate Response**: Uses Azure OpenAI to generate a response based on the embeddings and user query.
5. **Output Response**: Prints the generated response.
