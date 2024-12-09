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
    print("Connecting to database...\n")
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
        return None

# Main menu display
def displayMainMenu():
    print('------MENU------')
    print('  0. Settings')
    print('  1. Create Tables')
    print('  2. Exit')
    print('----------------')

# Terminal clearing function
def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def update_db_settings():
    global DB_HOST, DB_USER, DB_PASSWORD, DB_NAME
    
    print("------ Update Database Settings ------")
    DB_HOST = input(f"Enter database host (current: {DB_HOST}): ") or DB_HOST
    DB_USER = input(f"Enter database user (current: {DB_USER}): ") or DB_USER
    DB_PASSWORD = input(f"Enter database password (current: {DB_PASSWORD}): ") or DB_PASSWORD
    DB_NAME = input(f"Enter database name (current: {DB_NAME}): ") or DB_NAME

    print(f"\nUpdated settings: \nHost: {DB_HOST}\nUser: {DB_USER}\nPassword: {DB_PASSWORD}\nDatabase: {DB_NAME}\n")
    return get_db_connection()


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

# Menu function
# When run, displays menu options to a user
def run(conn):
    while conn is None:
        print("Error connecting to database, please update variables:\n")
        conn = update_db_settings()
    # Main menu loop
    while True:
        displayMainMenu()
        n = input("Enter option: ")
        info = ""
        try:
            n = int(n)
        except ValueError:
            info = "Invalid input. Please enter a number.\n"
        if n == 0:
            clear_screen()
            conn = update_db_settings()  # Update connection
        elif n == 1:
            clear_screen()
            createTables(conn)
        elif n == 2:
            clear_screen()
            print('Successfully Exited.')
            break  # Exit the loop
        else:
            clear_screen()
            print(info)


if __name__ == '__main__':
    conn = get_db_connection()
    run(conn)
