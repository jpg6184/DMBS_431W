# user.py
import bcrypt
import mysql.connector
import sql_commands
import DBMS_Program

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')

def verify_password(plain_password, hashed_password):
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

def create_user(conn):
    # Check if the users table is empty
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT COUNT(*) FROM users")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return
    result = cursor.fetchone()
    
    if result[0] == 0:
        # If table is empty then allow first user to be an admin
        print("No users found. The first user will be an admin.")
        username = input("Enter username: ")
        password = input("Enter password: ")
        hashed_password = hash_password(password)
        role = "admin"
        print(f"Creating admin user: {username}")
    else:
        # If the table is not empty, ask for admin credentials
        admin_password = input("Enter admin password: ")
        
        # Check if the provided admin password matches the stored password
        try:
            cursor.execute("SELECT hashed_password FROM users WHERE id = 1")
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return
        
        result = cursor.fetchone()
        
        if result and verify_password(admin_password, result[0]):
            # If the password is correct create user as admin
            print("Admin password verified.")
            username = input("Enter username: ")
            password = input("Enter password: ")
            hashed_password = hash_password(password)
            role = "admin"
        else:
            # If the password is incorrect, assign user as a guest
            print("Incorrect admin password. Creating user as guest.")
            username = input("Enter username: ")
            password = input("Enter password: ")
            hashed_password = hash_password(password)
            role = "guest"

    values = (username, hashed_password, role)
    
    try:
        cursor.execute(sql_commands.insert_user_sql, values)
        conn.commit()
        print(f"User '{username}' created successfully with role '{role}'.")
        cursor.close()
        return username, role
    except mysql.connector.Error as e:
        print(f"Error inserting user: {e}")
        cursor.close()
        return
    
def get_user_id(conn, username, password):
    try:
        cursor = conn.cursor()
        # Query to fetch the hashed password and ID for the given username
        cursor.execute("SELECT role, hashed_password FROM users WHERE username = %s", (username,))
        result = cursor.fetchone()
        if result:
            role, hashed_password = result
            # Verify the provided password against the hashed password
            if verify_password(password, hashed_password):
                return role
            else:
                print("Invalid password.")
        else:
            print("Username not found.")
    except mysql.connector.Error as e:
        print(f"Error fetching user: {e}")
    finally:
        cursor.close()

    return None

def change_user(conn, curr_user):
    while True:
        print("Changing user. Please log in.")
        username = input("Enter username: ")
        password = input("Enter password: ")

        # Fetch role and hashed password for the provided username
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT role, hashed_password FROM users WHERE username = %s", (username,))
            result = cursor.fetchone()

            if result:
                role, hashed_password = result

                # Verify the password
                if verify_password(password, hashed_password):
                    # Update globals and break the loop
                    DBMS_Program.clear_screen()
                    curr_user.update_user(username, role)
                    
                    print(username, role)
                    print(f"Logged in as {curr_user.get_username()} with role {curr_user.get_role()}.")
                    break
                else:
                    print("Invalid password. Please try again.")
            else:
                print("Username not found. Please try again.")
        except Exception as e:
            print(f"Error during login: {e}")
        finally:
            cursor.close()

    return
