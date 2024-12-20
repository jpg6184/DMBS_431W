import platform
import os
import run_IUD
import DBMS_Program
import user
import run_query

# Main menu display
# Terminal clearing function
def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def displayMainMenu():
    print('------MENU------')
    print('  0. Settings')
    print('  1. Create Tables (Admin)')
    print('  2. Insert Value (Admin)')
    print('  3. Update Value (Admin)')
    print('  4. Delete Value (Admin)')
    print('  5. Queries')
    print('  6. Exit')
    print('----------------')

def displaySettingsMenu():
    print('----SETTINGS----')
    print('  1. Update Database Connection')
    print('  2. Add User')
    print('  3. Change Current User')
    print('  4. Exit')
    print('----------------')

def displayInsertMenu():
    print('------INSERT MENU------')
    print('  1. Insert into Product')
    print('  2. Insert into Supplier')
    print('  3. Insert into Inventory')
    print('  4. Insert into Customer')
    print('  5. Insert into Transaction')
    print('  6. Insert into Discount')
    print('  7. Insert into Loyalty Program')
    print('  8. Insert into Employee')
    print('  9. Back to Main Menu')
    print('----------------')

def displayUpdateMenu():
    print('------UPDATE MENU------')
    print('  1. Update into Product')
    print('  2. Update into Supplier')
    print('  3. Update into Inventory')
    print('  4. Update into Customer')
    print('  5. Update into Transaction')
    print('  6. Update into Discount')
    print('  7. Update into Loyalty Program')
    print('  8. Update into Employee ')
    print('  9. Back to Main Menu')
    print('----------------')

def displayDeleteMenu():
    print('------DELETE MENU------')
    print('  1. Delete from Product')
    print('  2. Delete from Supplier')
    print('  3. Delete from Inventory')
    print('  4. Delete from Customer')
    print('  5. Delete from Transaction')
    print('  6. Delete from Discount')
    print('  7. Delete from Loyalty Program')
    print('  8. Delete from Employee ')
    print('  9. Back to Main Menu')
    print('----------------')

def displayQueryMenu():
    print('------QUERY MENU------')
    print('  1. View Products (Admin)')
    print('  2. View Suppliers (Admin)')
    print('  3. View Transactions (Admin)')
    print('  4. View Products by Supplier')
    print('  5. View Transactions by Customer')
    print('  6. View Products with Low Stock')
    print('  7. View Products by Total Revenue')
    print('  8. View Employees by Total Sales')
    print('  9. View Transaction Counts by Customer')
    print(' 10. View Profit Margins')
    print(' 11. View Products with Highest Discounts')
    print(' 12. View Top Customers by Spending')
    print(' 13. View Inventory Value')
    print('  0. Back to Main Menu')
    print('----------------')

def displayTransactionMenu():
    print('------TRANSACTION MENU------')
    print('  1. Add Transaction')
    print('  2. View Suppliers (Admin)')
    print('  3. View Transactions (Admin)')
    print('  4. View Products by Supplier')
    print('  5. View Transactions by Customer')
    print('  6. View Products with Low Stock')
    print('  7. View Products by Total Revenue')
    print('  8. View Employees by Total Sales')
    print('  9. View Transaction Counts by Customer')
    print('  0. Back to Main Menu')
    print('----------------')

def runInsertMenu(conn):
    while True:
        displayInsertMenu()
        n = input("Enter option: ")
        if n == '1':
            print("Inserting into Product...")
            run_IUD.prod_insert(conn)
        elif n == '2':
            print("Inserting into Supplier...")
            run_IUD.supplier_insert(conn)
        elif n == '3':
            print("Inserting into Inventory...")
            run_IUD.inventory_insert(conn)
        elif n == '4':
            print("Inserting into Customer...")
            run_IUD.customer_insert(conn)
        elif n == '5':
            print("Inserting into Transaction...")
            run_IUD.transaction_insert(conn)
        elif n == '6':
            print("Inserting into Discount...")
            run_IUD.discount_insert(conn)
        elif n == '7':
            print("Inserting into Loyalty Program...")
            run_IUD.loyalty_program_insert(conn)
        elif n == '8':
            print("Inserting into Employee...")
            run_IUD.employee_insert
        elif n == '9':
            print("Returning to Main Menu...\n")
            #displayMainMenu()
            break
        else:
            print("Invalid input. Please try again.\n")

def runUpdateMenu(conn):
    while True:
        displayUpdateMenu()
        n = input("Enter option: ")
        if n == '1':
            print("Updating Product...")
            run_IUD.prod_update(conn)
        elif n == '2':
            print("Updating Supplier...")
            run_IUD.supplier_update(conn)
        elif n == '3':
            print("Updating Inventory...")
            run_IUD.inventory_update(conn)
        elif n == '4':
            print("Updating Customer...")
            run_IUD.customer_update(conn)
        elif n == '5':
            print("Updating Transaction...")
            run_IUD.transaction_update(conn)
        elif n == '6':
            print("Updating Discount...")
            run_IUD.discount_update(conn)
        elif n == '7':
            print("Updating Loyalty Program...")
            run_IUD.loyalty_program_update(conn)
        elif n == '8':
            print("Updating Employee...")
            run_IUD.employee_update
        elif n == '9':
            print("Returning to Main Menu...\n")
            displayMainMenu()
            break
        else:
            print("Invalid input. Please try again.\n")

def runDeleteMenu(conn):
    while True:
        displayDeleteMenu()
        n = input("Enter option: ")
        if n == '1':
            print("Deleting Product...")
            run_IUD.prod_delete(conn)
        elif n == '2':
            print("Deleting Supplier...")
            run_IUD.supplier_delete(conn)
        elif n == '3':
            print("Deleting Inventory...")
            run_IUD.inventory_delete(conn)
        elif n == '4':
            print("Deleting Customer...")
            run_IUD.customer_delete(conn)
        elif n == '5':
            print("Deleting Transaction...")
            run_IUD.transaction_delete(conn)
        elif n == '6':
            print("Deleting Discount...")
            run_IUD.discount_delete(conn)
        elif n == '7':
            print("Deleting Loyalty Program...")
            run_IUD.loyalty_program_delete(conn)
        elif n == '8':
            print("Deleting Employee...")
            run_IUD.employee_delete(conn)
        elif n == '9':
            print("Returning to Main Menu...\n")
            displayMainMenu()
            break
        else:
            print("Invalid input. Please try again.\n")

def runSettingsMenu(conn, curr_user):
    while True:
        displaySettingsMenu()
        n = input("Enter Option: ")
        if n == '1':
            conn = DBMS_Program.update_db_settings(curr_user)
        elif n == '2':
            user.create_user(conn)
        elif n == '3':
            user.change_user(conn, curr_user)
        elif n == '4':
            break
        else:
            print('Invalid input. Please try again')

    return conn

def runQueryMenu(conn, curr_user):
    while True:
        displayQueryMenu()  # Display menu options
        n = input("Enter option: ")
        if n == '1':
            if curr_user.get_role() == 'admin':
                print("Displaying all products...\n")
                run_query.run_query_view_products(conn)
            else:
                print('You need admin access to perform this task.')
        elif n == '2':
            if curr_user.get_role() == 'admin':
                print("Displaying all suppliers...\n")
                run_query.run_query_view_suppliers(conn)
            else:
                print('You need admin access to perform this task.')
        elif n == '3':
            if curr_user.get_role() == 'admin':
                print("Displaying all transactions...\n")
                run_query.run_query_view_transactions(conn)
            else:
                print('You need admin access to perform this task.')
        elif n == '4':
            print("Displaying products by supplier...\n")
            run_query.run_query_view_products_by_supplier(conn)     
        elif n == '5':
            print("Displaying transactions by customer...\n")
            run_query.run_query_transactions_by_customer(conn)
        elif n == '6':
            print("Displaying products with low stock...\n")
            run_query.run_query_view_low_stock(conn)
        elif n == '7':
            print("Displaying products by total revenue...\n")
            run_query.run_query_view_product_by_revenue(conn)
        elif n == '8':
            print("Displaying employees ranked by total sales...\n")
            run_query.run_query_view_employee_by_sales(conn)
        elif n == '9':
            print("Displaying transaction counts by customer...\n")
            run_query.run_query_view_transaction_count_by_customer(conn)
        elif n == '10':
            print("Displaying profit margins...\n")
            run_query.run_query_view_profit_margins(conn)
        elif n == '11':
            print("Displaying products with highest discounts...\n")
            run_query.run_query_view_highest_discounts(conn)
        elif n == '12':
            print("Displaying top customers by spending...\n")
            run_query.run_query_view_customers_by_spending(conn)
        elif n == '13':
            print("Displaying inventory value...\n")
            run_query.run_query_view_inventory_value(conn)
        elif n == '0':
            print("Returning to Main Menu...\n")
            break
        else:
            print("Invalid input. Please try again.\n")
