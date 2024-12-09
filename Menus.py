import platform
import os

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
    print('  3. Exit')
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
    print('  8. add ')
    print('  9. Back to Main Menu')
    print('----------------')

def displayUpdateMenu():
    print('------INSERT MENU------')
    print('  1. Update into Product')
    print('  2. Update into Supplier')
    print('  3. Update into Inventory')
    print('  4. Update into Customer')
    print('  5. Update into Transaction')
    print('  6. Update into Discount')
    print('  7. Update into Loyalty Program')
    print('  8. add ')
    print('  9. Back to Main Menu')
    print('----------------')

def displayDeleteMenu():
    print('------INSERT MENU------')
    print('  1. Delete into Product')
    print('  2. Delete into Supplier')
    print('  3. Delete into Inventory')
    print('  4. Delete into Customer')
    print('  5. Delete into Transaction')
    print('  6. Delete into Discount')
    print('  7. Delete into Loyalty Program')
    print('  8. add ')
    print('  9. Back to Main Menu')
    print('----------------')

# Insert Menu function
# When run, displays menu options for Insert
def runInsertMenu(conn):
    while True:
        displayInsertMenu()
        n = input("Enter option: ")
        if n == '1':
            print("Inserting into Product...")
        elif n == '2':
            print("Inserting into Supplier...")
        elif n == '3':
            print("Inserting into Inventory...")
        elif n == '4':
            print("Inserting into Customer...")
        elif n == '5':
            print("Inserting into Transaction...")
        elif n == '6':
            print("Inserting into Discount...")
        elif n == '7':
            print("Inserting into Loyalty Program...")
        elif n == '8':
            print("TBD")
        elif n == '9':
            print("Returning to Main Menu...\n")
            displayMainMenu
            break
        else:
            print("Invalid input. Please try again.\n")

def runUpdateMenu(conn):
    while True:
        displayInsertMenu()
        n = input("Enter option: ")
        if n == '1':
            print("Updating into Product...")
        elif n == '2':
            print("Updating into Supplier...")
        elif n == '3':
            print("Updating into Inventory...")
        elif n == '4':
            print("Updating into Customer...")
        elif n == '5':
            print("Updating into Transaction...")
        elif n == '6':
            print("Updating into Discount...")
        elif n == '7':
            print("Updating into Loyalty Program...")
        elif n == '8':
            print("TBD")
        elif n == '9':
            print("Returning to Main Menu...\n")
            displayMainMenu
            break
        else:
            print("Invalid input. Please try again.\n")

def runDeleteMenu(conn):
    while True:
        displayInsertMenu()
        n = input("Enter option: ")
        if n == '1':
            print("Deleting into Product...")
        elif n == '2':
            print("Deleting into Supplier...")
        elif n == '3':
            print("Deleting into Inventory...")
        elif n == '4':
            print("Deleting into Customer...")
        elif n == '5':
            print("Deleting into Transaction...")
        elif n == '6':
            print("Deleting into Discount...")
        elif n == '7':
            print("Deleting into Loyalty Program...")
        elif n == '8':
            print("TBD")
        elif n == '9':
            print("Returning to Main Menu...\n")
            displayMainMenu
            break
        else:
            print("Invalid input. Please try again.\n")



