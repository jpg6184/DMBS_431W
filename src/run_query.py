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
        headers = ["Supplier ID", "Supplier Name", "Contact Number"]
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
        headers = ["Transaction ID", "Customer ID", "Product ID", "Date"]
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

def run_query_transactions_by_customer(conn):
    cursor = conn.cursor()
    try:
        cursor.execute(sql_commands.view_transactions_by_customer)
        transactions = cursor.fetchall()
        headers = ["Customer Name", "Product Name", "Total Price"]
        print(tabulate(transactions, headers=headers, tablefmt="grid"))
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()

def run_query_view_low_stock(conn):
    cursor = conn.cursor()
    try:
        cursor.execute(sql_commands.view_low_stock)
        low_stock = cursor.fetchall()
        headers = ["Product Name", "Stock Quantity"]
        print(tabulate(low_stock, headers=headers, tablefmt="grid"))
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()

def run_query_view_product_by_revenue(conn):
    cursor = conn.cursor()
    try:
        cursor.execute(sql_commands.view_product_by_revenue)
        products_revenue = cursor.fetchall()
        headers = ["Product Name", "Total Quantity Sold", "Total Revenue"]
        print(tabulate(products_revenue, headers=headers, tablefmt="grid"))
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()

def run_query_view_employee_by_sales(conn):
    cursor = conn.cursor()
    try:
        cursor.execute(sql_commands.view_employee_by_sales)
        employee_sales = cursor.fetchall()
        headers = ["Employee Name", "Total Transactions", "Total Sales"]
        print(tabulate(employee_sales, headers=headers, tablefmt="grid"))
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()

def run_query_view_transaction_count_by_customer(conn):
    cursor = conn.cursor()
    try:
        cursor.execute(sql_commands.view_transaction_count_by_customer)
        customer_purchases = cursor.fetchall()
        headers = ["Customer Name", "Total Purchases"]
        print(tabulate(customer_purchases, headers=headers, tablefmt="grid"))
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
