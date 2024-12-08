import mysql.connector
import os
import platform

# Setting database connection variables
DB_HOST = 'localhost'
DB_USER = 'user'
DB_PASSWORD = 'password'
DB_NAME = 'BusinessDB'

# Create connection to database
def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        return conn
    except mysql.connector.Error as e:
        print(f"Error connecting to database: {e}")
        exit(1)

# Main menu display
def displayMainMenu():
    print('------MENU------')
    print('  1. Create Tables')
    print('  2. Exit')
    print('----------------')

# Terminal clearing function
def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def read_sql_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Basic function to create tables in db
def createTables(conn):
    try:
        db = conn.cursor()

        # Use the specified database
        print(f'Using database: {DB_NAME}')
        sql = f'USE {DB_NAME}'
        db.execute(sql)
        
        print('Creating tables...\n')

        # Create table
        sql = read_sql_from_file('tables_config.sql')
        db.execute(sql)

        print('----SUCCESS----\nReturning to menu...')

    except mysql.connector.Error as e:
        print(f"----FAILURE----\nError while creating tables: {e}\nReturning to menu...\n")

    # Ensure the cursor is closed
    finally:
        db.close()  

    # Go back to menu
    run(conn)

# Menu function
# When run, displays menu options to a user
def run(conn):
    displayMainMenu()
    n = input("Enter option: ")
    info = ""
    try:
        n = int(n)
    except ValueError:
        info = "Invalid input. Please enter a number.\n"
    if n == 1:
        clear_screen()
        createTables(conn)
    elif n == 2:
        clear_screen()
        print('Successfully Exited.')
    else:
        clear_screen()
        print(info)
        run(conn)
        
    
if __name__ == '__main__':
    conn = get_db_connection()
    run(conn)
           
            
    
    