import os
import subprocess
import mysql.connector
from mysql.connector import Error


def create_connection(host_name, user_name, user_password):
    """
    Create a connection to MySQL server
    """
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("Connection to MySQL successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


def create_database(connection, query):
    """
    Create a database in MySQL
    """
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


def upgrade_database(tenant_id: str):
    """
    Upgrade the database for a tenant
    """
    os.environ["TENANT_ID"] = tenant_id

    subprocess.run(["alembic", "upgrade", "head"], capture_output=True, text=True, check=True)

    # try:
    #     subprocess.run(["alembic", "upgrade", "head"], capture_output=True, text=True, check=True)
    # except subprocess.CalledProcessError as e:
    #     print(f"Subprocess failed with return code {e.returncode}")
    #     print(f"Command: {e.cmd}")
    #     print(f"Output: {e.output}")
    #     print(f"Error: {e.stderr}")
    #     traceback.print_exc()  # Print the full traceback for debugging

