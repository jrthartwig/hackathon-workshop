# Product Anomaly Detection Lab

This lab will guide you through setting up Azure SQL servers, seeding data, generating embeddings using Azure OpenAI, and using Retrieval Augmented Generation (RAG) to detect anomalies in product data.

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

## 3. Copying Data from Source to Destination

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

## 4. Setup

### Step 1: Install Python on Windows
1. Download and install Python 3.7 or higher from the *An external link was removed to protect your privacy.*.

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

## 5. Add Embeddings Python Script

### Steps in `add-embeddings.py`
1. **Load Environment Variables**: The script loads environment variables from the `.env` file.
2. **Set Up Azure OpenAI Client**: Initializes the Azure OpenAI client using the API key and endpoint.
3. **Connect to Azure SQL**: Establishes a connection to the destination SQL database.
4. **Add Embedding Column**: Adds an `Embedding` column to the `SalesLT.SalesOrderDetail` table if it doesn't exist.
5. **Fetch Data**: Retrieves product data from the SQL database.
6. **Generate Embeddings**: Uses Azure OpenAI to generate embeddings for each product data row.
7. **Store Embeddings**: Stores the generated embeddings back in the SQL database.

## 6. Query Embeddings in Azure Query Editor

### Step 1: Query Embeddings
1. Navigate to your destination SQL database in the Azure Portal.
2. Open the **Query editor** and run a query to view the embeddings:
    ```sql
    SELECT TOP 10 ProductID, Embedding FROM SalesLT.SalesOrderDetail;
    ```

## 7. Chat with Data Python Script

### Steps in `chat-with-data.py`
1. **Load Environment Variables**: The script loads environment variables from the `.env` file.
2. **Fetch Embeddings**: Connects to the SQL database and retrieves the embeddings.
3. **Format Product Data**: Formats the product data for input into the Azure OpenAI model.
4. **Generate Response**: Uses Azure OpenAI to generate a response based on the embeddings and user query.
5. **Output Response**: Prints the generated response.
