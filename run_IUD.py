import sql_commands

# insert functions 

def prod_insert(conn):
    product_id = int(input("Enter product ID to insert: "))
    name = input("Enter product name: ")
    supplier_id = int(input("Enter supplier ID: "))
    buying_price = float(input("Enter buying price: "))
    selling_price = float(input("Enter selling price: "))
    
    cursor = conn.cursor()
    cursor.execute(sql_commands.insert_product_sql, (product_id, name, supplier_id, buying_price, selling_price))
    conn.commit()
    print(f"Product with ID {product_id} inserted successfully.")

def supplier_insert(conn):
    supplier_id = int(input("Enter supplier ID to insert: "))
    name = input("Enter supplier name: ")
    phone_number = input("Enter supplier phone number: ")
    
    cursor = conn.cursor()
    cursor.execute(sql_commands.insert_supplier_sql, (supplier_id, name, phone_number))
    conn.commit()
    print(f"Supplier with ID {supplier_id} inserted successfully.")

def customer_insert(conn):
    customer_id = int(input("Enter customer ID to insert: "))
    name = input("Enter customer name: ")
    email = input("Enter customer email: ")
    total_spent = float(input("Enter total spent: "))
    
    cursor = conn.cursor()
    cursor.execute(sql_commands.insert_customer_sql, (customer_id, name, email, total_spent))
    conn.commit()
    print(f"Customer with ID {customer_id} inserted successfully.")

def discount_insert(conn):
    discount_id = int(input("Enter discount ID to insert: "))
    product_id = int(input("Enter product ID for discount: "))
    discount_percentage = float(input("Enter discount percentage: "))
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    
    cursor = conn.cursor()
    cursor.execute(sql_commands.insert_discount_sql, (discount_id, product_id, discount_percentage, start_date, end_date))
    conn.commit()
    print(f"Discount with ID {discount_id} inserted successfully.")

def loyalty_program_insert(conn):
    loyalty_id = int(input("Enter loyalty ID to insert: "))
    discount_id = int(input("Enter discount ID for loyalty program: "))
    points_required = int(input("Enter points required: "))
    
    cursor = conn.cursor()
    cursor.execute(sql_commands.insert_loyalty_program_sql, (loyalty_id, discount_id, points_required))
    conn.commit()
    print(f"Loyalty Program with ID {loyalty_id} inserted successfully.")

def inventory_insert(conn):
    product_id = int(input("Enter product ID for inventory: "))
    quantity = int(input("Enter product quantity: "))
    
    cursor = conn.cursor()
    cursor.execute(sql_commands.insert_inventory_sql, (product_id, quantity))
    conn.commit()
    print(f"Inventory for product ID {product_id} inserted successfully.")

def transaction_insert(conn):
    transaction_id = int(input("Enter transaction ID to insert: "))
    customer_id = int(input("Enter customer ID: "))
    product_id = int(input("Enter product ID: "))
    quantity = int(input("Enter quantity: "))
    date = input("Enter transaction date (YYYY-MM-DD): ")
    
    cursor = conn.cursor()
    cursor.execute(sql_commands.insert_transaction_sql, (transaction_id, customer_id, product_id, quantity, date))
    conn.commit()
    print(f"Transaction with ID {transaction_id} inserted successfully.")

def employee_insert(conn): 
    employee_id = int(input("Enter employee ID to insert: "))
    name = input("Enter employee name =")

    cursor = conn.cursor()
    cursor.execute(sql_commands.insert_employee_sql, (employee_id, name))
    conn.commit()
    print(f"Transaction with ID {employee_id} inserted successfully.")

# Update Functions

def prod_update(conn):
    product_id = int(input("Enter product ID to update: "))
    name = input("Enter new product name: ")
    supplier_id = int(input("Enter new supplier ID: "))
    buying_price = float(input("Enter new buying price: "))
    selling_price = float(input("Enter new selling price: "))
    
    cursor = conn.cursor()
    cursor.execute(sql_commands.update_product_sql, (name, supplier_id, buying_price, selling_price, product_id))
    conn.commit()
    print(f"Product with ID {product_id} updated successfully.")

def supplier_update(conn):
    supplier_id = int(input("Enter supplier ID to update: "))
    name = input("Enter new supplier name: ")
    phone_number = input("Enter new supplier phone number: ")
    
    cursor = conn.cursor()
    cursor.execute(sql_commands.update_supplier_sql, (name, phone_number, supplier_id))
    conn.commit()
    print(f"Supplier with ID {supplier_id} updated successfully.")

def customer_update(conn):
    customer_id = int(input("Enter customer ID to update: "))
    name = input("Enter new customer name: ")
    email = input("Enter new customer email: ")
    total_spent = float(input("Enter new total spent: "))
    
    cursor = conn.cursor()
    cursor.execute(sql_commands.update_customer_sql, (name, email, total_spent, customer_id))
    conn.commit()
    print(f"Customer with ID {customer_id} updated successfully.")

def discount_update(conn):
    discount_id = int(input("Enter discount ID to update: "))
    product_id = int(input("Enter new product ID for discount: "))
    discount_percentage = float(input("Enter new discount percentage: "))
    start_date = input("Enter new start date (YYYY-MM-DD): ")
    end_date = input("Enter new end date (YYYY-MM-DD): ")
    
    cursor = conn.cursor()
    cursor.execute(sql_commands.update_discount_sql, (product_id, discount_percentage, start_date, end_date, discount_id))
    conn.commit()
    print(f"Discount with ID {discount_id} updated successfully.")

def loyalty_program_update(conn):
    loyalty_id = int(input("Enter loyalty ID to update: "))
    discount_id = int(input("Enter new discount ID for loyalty program: "))
    points_required = int(input("Enter new points required: "))
    
    cursor = conn.cursor()
    cursor.execute(sql_commands.update_loyalty_program_sql, (discount_id, points_required, loyalty_id))
    conn.commit()
    print(f"Loyalty Program with ID {loyalty_id} updated successfully.")

def inventory_update(conn):
    product_id = int(input("Enter product ID for inventory update: "))
    quantity = int(input("Enter new product quantity: "))
    
    cursor = conn.cursor()
    cursor.execute(sql_commands.update_inventory_sql, (quantity, product_id))
    conn.commit()
    print(f"Inventory for product ID {product_id} updated successfully.")

def transaction_update(conn):
    transaction_id = int(input("Enter transaction ID to update: "))
    customer_id = int(input("Enter new customer ID: "))
    product_id = int(input("Enter new product ID: "))
    quantity = int(input("Enter new quantity: "))
    date = input("Enter new transaction date (YYYY-MM-DD): ")
    
    cursor = conn.cursor()
    cursor.execute(sql_commands.update_transaction_sql, (customer_id, product_id, quantity, date, transaction_id))
    conn.commit()
    print(f"Transaction with ID {transaction_id} updated successfully.")

def employee_update(conn):
    employee_id = int(input("Enter employee ID to update: "))
    name = input("Enter new employee name: ")
    
    cursor = conn.cursor()
    cursor.execute(sql_commands.update_employee_sql, (name, employee_id))
    conn.commit()
    print(f"Employee with ID {employee_id} updated successfully.")


# Delete Functions

def prod_delete(conn):
    product_id = int(input("Enter product ID to delete: "))
    
    cursor = conn.cursor()
    cursor.execute(sql_commands.delete_product_sql, (product_id,))
    conn.commit()
    print(f"Product with ID {product_id} deleted successfully.")

def supplier_delete(conn):
    supplier_id = int(input("Enter supplier ID to delete: "))
    
    cursor = conn.cursor()
    cursor.execute(sql_commands.delete_supplier_sql, (supplier_id,))
    conn.commit()
    print(f"Supplier with ID {supplier_id} deleted successfully.")

def customer_delete(conn):
    customer_id = int(input("Enter customer ID to delete: "))
    
    cursor = conn.cursor()
    cursor.execute(sql_commands.delete_customer_sql, (customer_id,))
    conn.commit()
    print(f"Customer with ID {customer_id} deleted successfully.")

def discount_delete(conn):
    discount_id = int(input("Enter discount ID to delete: "))
    
    cursor = conn.cursor()
    cursor.execute(sql_commands.delete_discount_sql, (discount_id,))
    conn.commit()
    print(f"Discount with ID {discount_id} deleted successfully.")

def loyalty_program_delete(conn):
    loyalty_id = int(input("Enter loyalty ID to delete: "))
    
    cursor = conn.cursor()
    cursor.execute(sql_commands.delete_loyalty_program_sql, (loyalty_id,))
    conn.commit()
    print(f"Loyalty Program with ID {loyalty_id} deleted successfully.")

def inventory_delete(conn):
    product_id = int(input("Enter product ID for inventory deletion: "))
    
    cursor = conn.cursor()
    cursor.execute(sql_commands.delete_inventory_sql, (product_id,))
    conn.commit()
    print(f"Inventory for product ID {product_id} deleted successfully.")

def transaction_delete(conn):
    transaction_id = int(input("Enter transaction ID to delete: "))
    
    cursor = conn.cursor()
    cursor.execute(sql_commands.delete_transaction_sql, (transaction_id,))
    conn.commit()
    print(f"Transaction with ID {transaction_id} deleted successfully.")

def employee_delete(conn):
    employee_id = int(input("Enter employee ID to delete: "))
    
    cursor = conn.cursor()
    cursor.execute(sql_commands.delete_employee_sql, (employee_id,))
    conn.commit()
    print(f"Employee with ID {employee_id} deleted successfully.")
