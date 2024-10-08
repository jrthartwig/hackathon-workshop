## 1. Sign Up for GitHub

### Step 1: Create a GitHub Account
1. Go to [github.com](https://github.com/).
2. Click on **Sign up** and follow the instructions to create a new account.
3. Verify your email address to complete the sign-up process.

## 2. Install Visual Studio Code (VS Code)

### For Windows
1. Go to the [Visual Studio Code Downloads](https://code.visualstudio.com/download).
2. Download the **Windows** installer.
3. Run the installer and follow the instructions to complete the installation.

### For macOS
1. Go to the [Visual Studio Code Downloads](https://code.visualstudio.com/download).
2. Download the **macOS** installer.
3. Open the downloaded file and drag the **Visual Studio Code** icon to the **Applications** folder.

## 3. Install ODBC Driver for SQL Server 18

### For Windows
1. Go to the *An external link was removed to protect your privacy.*.
2. Download the **ODBC Driver 18 for SQL Server** for Windows.
3. Run the installer and follow the instructions to complete the installation.

### For macOS
1. Open a terminal and run the following commands to install the ODBC driver:
    ```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
    brew tap microsoft/mssql-release https://github.com/Microsoft/homebrew-mssql-release
    brew update
    HOMEBREW_ACCEPT_EULA=Y brew install msodbcsql18 mssql-tools18
    ```

## 4. Install Python

### For Windows
1. Go to [Python Downloads](https://www.python.org/downloads/)
2. Download the **Windows** installer for Python 3.7 or higher.
3. Run the installer and make sure to check the box that says **Add Python to PATH**.
4. Follow the instructions to complete the installation.

### For macOS
1. Open a terminal and run the following command to install Python using Homebrew:
    ```bash
    (brew --prefix python)/libexec/bin
    ```

## 5. Install Git SCM

### For Windows
1. Go to the GitSCM https://git-scm.com/downloads.
2. Download the **Windows** installer.
3. Run the installer and follow the instructions to complete the installation.

### For macOS
1. Open a terminal and run the following command to install Git using Homebrew:
    ```bash
    brew install git
    ```

## 6. Clone the Repository

### Step 1: Open VS Code
1. Open **Visual Studio Code**.

### Step 2: Open Terminal in VS Code
1. Go to **View** > **Terminal** to open a new terminal window.

### Step 3: Clone the Repository
1. Run the following commands in the terminal to clone the repository:
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

## 7. Set Up a Virtual Environment

### Step 1: Create a Virtual Environment
1. Run the following command in the terminal:
    ```bash
    python -m venv venv
    ```

### Step 2: Activate the Virtual Environment
1. On Windows:
    ```bash
    venv\Scripts\activate
    ```
2. On macOS/Linux:
    ```bash
    source venv/bin/activate
    ```

## 8. Install Required Packages

### Step 1: Install Packages
1. Run the following command in the terminal:
    ```bash
    pip install -r requirements.txt
    ```