import sql_commands

def prod_insert(conn):
    print("Re-enter values to keep same")
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
    print("Re-enter values to keep same")
    supplier_id = int(input("Enter supplier ID to insert: "))
    name = input("Enter supplier name: ")
    phone_number = input("Enter supplier phone number: ")
    
    cursor = conn.cursor()
    cursor.execute(sql_commands.insert_supplier_sql, (supplier_id, name, phone_number))
    conn.commit()
    print(f"Supplier with ID {supplier_id} inserted successfully.")

def customer_insert(conn):
    print("Re-enter values to keep same")
    customer_id = int(input("Enter customer ID to insert: "))
    name = input("Enter customer name: ")
    email = input("Enter customer email: ")
    total_spent = float(input("Enter total spent: "))
    
    cursor = conn.cursor()
    cursor.execute(sql_commands.insert_customer_sql, (customer_id, name, email, total_spent))
    conn.commit()
    print(f"Customer with ID {customer_id} inserted successfully.")

def discount_insert(conn):
    print("Re-enter values to keep same")
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
    print("Re-enter values to keep same")
    loyalty_id = int(input("Enter loyalty ID to insert: "))
    discount_id = int(input("Enter discount ID for loyalty program: "))
    points_required = int(input("Enter points required: "))
    
    cursor = conn.cursor()
    cursor.execute(sql_commands.insert_loyalty_program_sql, (loyalty_id, discount_id, points_required))
    conn.commit()
    print(f"Loyalty Program with ID {loyalty_id} inserted successfully.")

def inventory_insert(conn):
    print("Re-enter values to keep same")
    product_id = int(input("Enter product ID for inventory: "))
    quantity = int(input("Enter product quantity: "))
    
    cursor = conn.cursor()
    cursor.execute(sql_commands.insert_inventory_sql, (product_id, quantity))
    conn.commit()
    print(f"Inventory for product ID {product_id} inserted successfully.")

def transaction_insert(conn):
    print("Re-enter values to keep same")
    transaction_id = int(input("Enter transaction ID to insert: "))
    customer_id = int(input("Enter customer ID: "))
    product_id = int(input("Enter product ID: "))
    quantity = int(input("Enter quantity: "))
    date = input("Enter transaction date (YYYY-MM-DD): ")
    
    cursor = conn.cursor()
    cursor.execute(sql_commands.insert_transaction_sql, (transaction_id, customer_id, product_id, quantity, date))
    conn.commit()
    print(f"Transaction with ID {transaction_id} inserted successfully.")
