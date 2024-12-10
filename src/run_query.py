import mysql.connector
import sql_commands
from tabulate import tabulate

def run_query_view_products(conn):
    cursor = conn.cursor()
    try:
        cursor.execute(sql_commands.view_products_sql)
        products = cursor.fetchall()
        
        # Define headers for the table
        headers = ["Product ID", "Product Name", "Supplier ID", "Buying Price", "Selling Price"]
        
        # Print the table using tabulate
        print(tabulate(products, headers=headers, tablefmt="pretty", floatfmt=".2f"))
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()

def run_query_view_suppliers(conn):
    cursor = conn.cursor()
    try:
        cursor.execute(sql_commands.view_suppliers_sql)
        suppliers = cursor.fetchall()
        
        # Define headers for the table
        headers = ["Supplier ID", "Supplier Name", "Contact Number"]
        
        # Print the table using tabulate
        print(tabulate(suppliers, headers=headers, tablefmt="pretty"))
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()

def run_query_view_transactions(conn):
    cursor = conn.cursor()
    try:
        cursor.execute(sql_commands.view_transactions_sql)
        transactions = cursor.fetchall()
        
        # Define headers for the table
        headers = ["Transaction ID", "Customer ID", "Product ID", "Date"]
        
        # Print the table using tabulate
        print(tabulate(transactions, headers=headers, tablefmt="pretty", floatfmt=".2f"))
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()

def run_query_view_products_by_supplier(conn):
    cursor = conn.cursor()
    try:
        cursor.execute(sql_commands.view_products_by_supplier_sql)
        products = cursor.fetchall()
        
        # Define headers for the table
        headers = ["Product ID", "Product Name", "Supplier Name", "Buying Price", "Selling Price"]
        
        # Print the table using tabulate
        print(tabulate(products, headers=headers, tablefmt="pretty", floatfmt=".2f"))
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
