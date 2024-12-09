import sql_commands
import user
import mysql.connector

def get_input(prompt, expected_type):
    while True:
        try:
            user_input = input(prompt)
            # Attempt to cast input to expected type
            if expected_type == int:
                return int(user_input)
            elif expected_type == float:
                return float(user_input)
            else:
                return user_input
        except ValueError:
            print(f"Invalid input. Please enter a valid {expected_type.__name__}.\n")

# insert functions 

def prod_insert(conn):
    product_id = get_input("Enter product ID to insert: ", int)
    name = input("Enter product name: ")
    supplier_id = get_input("Enter supplier ID: ", int)
    buying_price = get_input("Enter buying price: ", float)
    selling_price = get_input("Enter selling price: ", float)
    
    cursor = conn.cursor()
    cursor.execute(sql_commands.insert_product_sql, (product_id, name, supplier_id, buying_price, selling_price))
    conn.commit()
    print(f"Product with ID {product_id} inserted successfully.")

def supplier_insert(conn):
    supplier_id = get_input("Enter supplier ID to insert: ", int)
    name = input("Enter supplier name: ")
    phone_number = input("Enter supplier phone number: ")
    
    cursor = conn.cursor()
    cursor.execute(sql_commands.insert_supplier_sql, (supplier_id, name, phone_number))
    conn.commit()
    print(f"Supplier with ID {supplier_id} inserted successfully.")

def customer_insert(conn):
    customer_id = get_input("Enter customer ID to insert: ", int)
    name = input("Enter customer name: ")
    email = input("Enter customer email: ")
    total_spent = get_input("Enter total spent: ", float)
    
    cursor = conn.cursor()
    cursor.execute(sql_commands.insert_customer_sql, (customer_id, name, email, total_spent))
    conn.commit()
    print(f"Customer with ID {customer_id} inserted successfully.")

def discount_insert(conn):
    discount_id = get_input("Enter discount ID to insert: ", int)
    product_id = get_input("Enter product ID for discount: ", int)
    discount_percentage = get_input("Enter discount percentage: ", float)
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    
    cursor = conn.cursor()
    cursor.execute(sql_commands.insert_discount_sql, (discount_id, product_id, discount_percentage, start_date, end_date))
    conn.commit()
    print(f"Discount with ID {discount_id} inserted successfully.")

def loyalty_program_insert(conn):
    loyalty_id = get_input("Enter loyalty ID to insert: ", int)
    discount_id = get_input("Enter discount ID for loyalty program: ", int)
    points_required = get_input("Enter points required: ", int)
    
    cursor = conn.cursor()
    cursor.execute(sql_commands.insert_loyalty_program_sql, (loyalty_id, discount_id, points_required))
    conn.commit()
    print(f"Loyalty Program with ID {loyalty_id} inserted successfully.")

def inventory_insert(conn):
    product_id = get_input("Enter product ID for inventory: ", int)
    quantity = get_input("Enter product quantity: ", int)
    
    cursor = conn.cursor()
    cursor.execute(sql_commands.insert_inventory_sql, (product_id, quantity))
    conn.commit()
    print(f"Inventory for product ID {product_id} inserted successfully.")

def transaction_insert(conn):
    transaction_id = get_input("Enter transaction ID to insert: ", int)
    customer_id = get_input("Enter customer ID: ", int)
    product_id = get_input("Enter product ID: ", int)
    quantity = get_input("Enter quantity: ", int)
    date = input("Enter transaction date (YYYY-MM-DD): ")
    
    cursor = conn.cursor()
    cursor.execute(sql_commands.insert_transaction_sql, (transaction_id, customer_id, product_id, quantity, date))
    conn.commit()
    print(f"Transaction with ID {transaction_id} inserted successfully.")

def employee_insert(conn): 
    employee_id = get_input("Enter employee ID to insert: ", int)
    name = input("Enter employee name: ")

    cursor = conn.cursor()
    cursor.execute(sql_commands.insert_employee_sql, (employee_id, name))
    conn.commit()
    print(f"Transaction with ID {employee_id} inserted successfully.")

def create_user(conn):
    # Check if the users table is empty
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM users")
    result = cursor.fetchone()
    
    if result[0] == 0:
        # If the table is empty then allow the first user to be an admin
        print("No users found. The first user will be an admin.")
        username = input("Enter username: ")
        password = input("Enter password: ")
        hashed_password = user.hash_password(password)
        role = "admin"
        print(f"Creating admin user: {username}")
    else:
        # If the table is not empty, ask for admin credentials
        admin_password = input("Enter admin password: ")
        hashed_admin_password = user.hash_password(admin_password)
        
        # Check if the provided admin password matches the stored password
        cursor.execute("SELECT password FROM users WHERE id = 1")
        result = cursor.fetchone()
        
        if result and result[0] == hashed_admin_password:
            # If the password is correct create user as admin
            print("Admin password verified.")
            username = input("Enter username: ")
            password = input("Enter password: ")
            hashed_password = user.hash_password(password)
            role = "admin"
        else:
            # If the password is incorrect, assign user as a guest
            print("Incorrect admin password. Creating user as guest.")
            username = input("Enter username: ")
            password = input("Enter password: ")
            hashed_password = user.hash_password(password)
            role = "guest"

    values = (username, hashed_password, role)
    
    try:
        print(values)
        cursor.execute(sql_commands.insert_user_sql, values)
        print(f"User '{username}' created successfully with role '{role}'.")
    except mysql.connector.Error as e:
        print(f"Error inserting user: {e}")
    finally:
        conn.commit()
        cursor.close()

# Update Functions

def prod_update(conn):
    product_id = get_input("Enter product ID to update: ", int)
    name = input("Enter new product name: ")
    supplier_id = get_input("Enter new supplier ID: ", int)
    buying_price = get_input("Enter new buying price: ", float)
    selling_price = get_input("Enter new selling price: ", float)
    
    cursor = conn.cursor()
    cursor.execute(sql_commands.update_product_sql, (name, supplier_id, buying_price, selling_price, product_id))
    print(cursor.fetchwarnings())

    conn.commit()
    print(f"Product with ID {product_id} updated successfully.")

def supplier_update(conn):
    supplier_id = get_input("Enter supplier ID to update: ", int)
    name = input("Enter new supplier name: ")
    phone_number = input("Enter new supplier phone number: ")
    
    cursor = conn.cursor()
    cursor.execute(sql_commands.update_supplier_sql, (name, phone_number, supplier_id))
    conn.commit()
    print(f"Supplier with ID {supplier_id} updated successfully.")

def customer_update(conn):
    customer_id = get_input("Enter customer ID to update: ", int)
    name = input("Enter new customer name: ")
    email = input("Enter new customer email: ")
    total_spent = get_input("Enter new total spent: ", float)
    
    cursor = conn.cursor()
    cursor.execute(sql_commands.update_customer_sql, (name, email, total_spent, customer_id))
    conn.commit()
    print(f"Customer with ID {customer_id} updated successfully.")

def discount_update(conn):
    discount_id = get_input("Enter discount ID to update: ", int)
    product_id = get_input("Enter new product ID for discount: ", int)
    discount_percentage = get_input("Enter new discount percentage: ", float)
    start_date = input("Enter new start date (YYYY-MM-DD): ")
    end_date = input("Enter new end date (YYYY-MM-DD): ")
    
    cursor = conn.cursor()
    cursor.execute(sql_commands.update_discount_sql, (product_id, discount_percentage, start_date, end_date, discount_id))
    conn.commit()
    print(f"Discount with ID {discount_id} updated successfully.")

def loyalty_program_update(conn):
    loyalty_id = get_input("Enter loyalty ID to update: ", int)
    discount_id = get_input("Enter new discount ID for loyalty program: ", int)
    points_required = get_input("Enter new points required: ", int)
    
    cursor = conn.cursor()
    cursor.execute(sql_commands.update_loyalty_program_sql, (discount_id, points_required, loyalty_id))
    conn.commit()
    print(f"Loyalty Program with ID {loyalty_id} updated successfully.")

def inventory_update(conn):
    product_id = get_input("Enter product ID for inventory update: ", int)
    quantity = get_input("Enter new product quantity: ", int)
    
    cursor = conn.cursor()
    cursor.execute(sql_commands.update_inventory_sql, (quantity, product_id))
    conn.commit()
    print(f"Inventory for product ID {product_id} updated successfully.")

def transaction_update(conn):
    transaction_id = get_input("Enter transaction ID to update: ", int)
    customer_id = get_input("Enter new customer ID: ", int)
    product_id = get_input("Enter new product ID: ", int)
    quantity = get_input("Enter new quantity: ", int)
    date = input("Enter new transaction date (YYYY-MM-DD): ")
    
    cursor = conn.cursor()
    cursor.execute(sql_commands.update_transaction_sql, (customer_id, product_id, quantity, date, transaction_id))
    conn.commit()
    print(f"Transaction with ID {transaction_id} updated successfully.")

def employee_update(conn):
    employee_id = get_input("Enter employee ID to update: ", int)
    name = input("Enter new employee name: ")
    
    cursor = conn.cursor()
    cursor.execute(sql_commands.update_employee_sql, (name, employee_id))
    conn.commit()
    print(f"Employee with ID {employee_id} updated successfully.")


# Delete Functions

def prod_delete(conn):
    product_id = get_input("Enter product ID to delete: ", int)
    
    cursor = conn.cursor()
    cursor.execute(sql_commands.delete_product_sql, (product_id,))
    conn.commit()
    print(f"Product with ID {product_id} deleted successfully.")

def supplier_delete(conn):
    supplier_id = get_input("Enter supplier ID to delete: ", int)
    
    cursor = conn.cursor()
    cursor.execute(sql_commands.delete_supplier_sql, (supplier_id,))
    conn.commit()
    print(f"Supplier with ID {supplier_id} deleted successfully.")

def customer_delete(conn):
    customer_id = get_input("Enter customer ID to delete: ", int)
    
    cursor = conn.cursor()
    cursor.execute(sql_commands.delete_customer_sql, (customer_id,))
    conn.commit()
    print(f"Customer with ID {customer_id} deleted successfully.")

def discount_delete(conn):
    discount_id = get_input("Enter discount ID to delete: ", int)
    
    cursor = conn.cursor()
    cursor.execute(sql_commands.delete_discount_sql, (discount_id,))
    conn.commit()
    print(f"Discount with ID {discount_id} deleted successfully.")

def loyalty_program_delete(conn):
    loyalty_id = get_input("Enter loyalty ID to delete: ", int)
    
    cursor = conn.cursor()
    cursor.execute(sql_commands.delete_loyalty_program_sql, (loyalty_id,))
    conn.commit()
    print(f"Loyalty Program with ID {loyalty_id} deleted successfully.")

def inventory_delete(conn):
    product_id = get_input("Enter product ID for inventory deletion: ", int)
    
    cursor = conn.cursor()
    cursor.execute(sql_commands.delete_inventory_sql, (product_id,))
    conn.commit()
    print(f"Inventory for product ID {product_id} deleted successfully.")

def transaction_delete(conn):
    transaction_id = get_input("Enter transaction ID to delete: ", int)
    
    cursor = conn.cursor()
    cursor.execute(sql_commands.delete_transaction_sql, (transaction_id,))
    conn.commit()
    print(f"Transaction with ID {transaction_id} deleted successfully.")

def employee_delete(conn):
    employee_id = get_input("Enter employee ID to delete: ", int)
    
    cursor = conn.cursor()
    cursor.execute(sql_commands.delete_employee_sql, (employee_id,))
    conn.commit()
    print(f"Employee with ID {employee_id} deleted successfully.")
    