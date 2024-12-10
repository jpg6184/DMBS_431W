import platform
import os
import run_IUD
import DBMS_Program
import user

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
    print('  1. Create Tables')
    print('  2. Insert Value')
    print('  3. Update Value')
    print('  4. Delete Value')
    print('  5. Exit')
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
            print("Inserting into Employee")
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
            print("Updating into Employee")
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
            print("Deleting into Employee")
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
