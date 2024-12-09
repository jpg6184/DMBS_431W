import mysql.connector
import user

def get_user_id(conn, username, password):
    try:
        cursor = conn.cursor()
        # Query to fetch the hashed password and ID for the given username
        cursor.execute("SELECT role, hashed_password FROM users WHERE username = %s", (username,))
        result = cursor.fetchone()
        if result:
            role, hashed_password = result
            # Verify the provided password against the hashed password
            if user.verify_password(password, hashed_password):
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