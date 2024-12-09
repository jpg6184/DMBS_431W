import mysql.connector
import os
import platform
import menu_handler
import run_IUD
import user

import run_read

# Setting database connection variables
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = '12345678'
DB_NAME = 'sampleDB'

USER_NAME = ''
USER_ROLE = ''

# Manage requests to create a new database
def create_database(db_name):
    """Function to create a new database."""
    global USER_NAME
    global USER_ROLE
    try:
        conn = mysql.connector.connect(
            host = DB_HOST,
            user = DB_USER,
            password = DB_PASSWORD
        )
        cursor = conn.cursor()
        cursor.execute(f"CREATE DATABASE {db_name}")
        clear_screen()
        print(f"Database '{db_name}' created successfully, populating tables...")
        conn.commit()
        cursor.close()

        conn.close()
        conn = mysql.connector.connect(
            host = DB_HOST,
            user = DB_USER,
            password = DB_PASSWORD,
            database = db_name
        )
        createTables(conn)
        result = run_IUD.create_user(conn)
        if result:
            USER_NAME = result[0]
            USER_ROLE = result[1]
        conn.close()
        return False
    except mysql.connector.Error as e:
        print(f"Error creating database: {e}")
        return True
        

# Create connection to database
def get_db_connection():
    global DB_NAME  # Access the global variable to modify it if necessary
    
    print(f"Current database is {DB_NAME}")
    while True:
        n = input("Is this correct? (y/n): ")
        if n == 'y' or n == "Y":
            running = True
            while running:
                create_new_db = input(f"Do you want to create a new database '{DB_NAME}'? (y/n): ")
                if create_new_db == 'y' or create_new_db == 'Y':
                    running = create_database(DB_NAME)
                elif create_new_db == 'n' or create_new_db == 'N':
                    running = False
            
            break 
        elif n == 'n' or n == 'N':
            running = True
            while running:
                DB_NAME = input("Enter database name: ")
                # Ask if user wants to create a new database
                create_new_db = input(f"Do you want to create a new database '{DB_NAME}'? (y/n): ")
                if create_new_db == 'y' or create_new_db == 'Y':
                    running = create_database(DB_NAME)
                elif create_new_db == 'n' or create_new_db == 'N':
                    running = False
            break

    print("Connecting to server...\n")
    try:
        conn = mysql.connector.connect(
            host = DB_HOST,
            user = DB_USER,
            password = DB_PASSWORD,
            database = DB_NAME
        )
        return conn
    except mysql.connector.Error as e:
        clear_screen()
        print(f"Error connecting to database: {e}")
        return None
    

# Terminal clearing function
def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def update_db_settings():
    global DB_HOST, DB_USER, DB_PASSWORD, DB_NAME
    
    print("------ Update Database Settings ------\n(Leave blank for same)")
    DB_HOST = input(f"Enter database host (current: {DB_HOST}): ") or DB_HOST
    DB_USER = input(f"Enter database user (current: {DB_USER}): ") or DB_USER
    DB_PASSWORD = input(f"Enter database password (current: {DB_PASSWORD}): ") or DB_PASSWORD
    DB_NAME = input(f"Enter database name (current: {DB_NAME}): ") or DB_NAME

    clear_screen()
    print(f"\nUpdated settings: \nHost: {DB_HOST}\nUser: {DB_USER}\nPassword: {DB_PASSWORD}\nDatabase: {DB_NAME}\n")
    return get_db_connection()


def read_sql_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Basic function to create tables in db
def createTables(conn):
    try:
        cursor = conn.cursor()

        # Use the specified database
        print(f'Using database: {DB_NAME}')
        sql = f'USE {DB_NAME}'
        cursor.execute(sql)
        conn.commit()
        print('Creating tables...\n')

        # Create table
        sql = read_sql_from_file('tables_config.sql')
        for result in cursor.execute(sql, multi=True): 
            # Consume any results before committing
            if result.with_rows: 
                print(result)
                result.fetchall() 
        conn.commit()
        
        print('----SUCCESS----')

    except mysql.connector.Error as e:
        print(f"----FAILURE----")

    # Ensure cursor is closed
    finally:
        
        if cursor:
            cursor.close()



# Menu function
# When run, displays menu options to a user
def run(conn):
    global USER_NAME
    global USER_ROLE
    while conn is None:
        print("Please update variables:\n")
        conn = update_db_settings()
    # Main menu loop
    while USER_NAME == '':
        print("We don't know who you are.")
        username = input("Enter username: ")
        password = input("Enter password: ")
        role = run_read.get_user_id(conn, username, password)
        if role != None:
            USER_NAME = username
            USER_ROLE = role
    while True:
        clear_screen()
        print(f"Current User Role: {USER_ROLE}")
        menu_handler.displayMainMenu()
        n = input("Enter option: ")
        info = ""
        try:
            n = int(n)
        except ValueError:
            info = "Invalid input. Please enter a number.\n"
        if n == 0:
            clear_screen()
            conn = menu_handler.runSettingsMenu(conn)  # Update connection
        elif n == 1:
            clear_screen()
            createTables(conn)
        elif n == 2: 
            clear_screen()
            menu_handler.runInsertMenu(conn)
        elif n == 3: 
            clear_screen()
            menu_handler.runUpdateMenu(conn)
        elif n == 4: 
            clear_screen()
            menu_handler.runDeleteMenu(conn)
        elif n == 5:
            clear_screen()
            print('Successfully Exited.')
            break  # Exit the loop
        else:
            clear_screen()
            print(info)



if __name__ == '__main__':

    conn = get_db_connection()
    run(conn)
