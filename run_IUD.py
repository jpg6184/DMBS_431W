import sql_commands

def insert_product(conn, product_id, name, supplier_id, buying_price, selling_price):
    cursor = conn.cursor()
    cursor.execute(sql_commands.insert_product_sql, (product_id, name, supplier_id, buying_price, selling_price))
    conn.commit()
    print(f"Product {name} inserted successfully.")

def insert_supplier(conn, supplier_id, name, phone_number):
    cursor = conn.cursor()
    cursor.execute(sql_commands.insert_supplier_sql, (supplier_id, name, phone_number))
    conn.commit()
    print(f"Supplier {name} inserted successfully.")

def insert_customer(conn, customer_id, name, email, total_spent):
    cursor = conn.cursor()
    cursor.execute(sql_commands.insert_customer_sql, (customer_id, name, email, total_spent))
    conn.commit()
    print(f"Customer {name} inserted successfully.")

def insert_discount(conn, discount_id, product_id, discount_percentage, start_date, end_date):
    cursor = conn.cursor()
    cursor.execute(sql_commands.insert_discount_sql, (discount_id, product_id, discount_percentage, start_date, end_date))
    conn.commit()
    print(f"Discount for product ID {product_id} inserted successfully.")

def insert_loyalty_program(conn, loyalty_id, discount_id, points_required):
    cursor = conn.cursor()
    cursor.execute(sql_commands.insert_loyalty_program_sql, (loyalty_id, discount_id, points_required))
    conn.commit()
    print(f"Loyalty Program {loyalty_id} inserted successfully.")

def insert_inventory(conn, product_id, quantity):
    cursor = conn.cursor()
    cursor.execute(sql_commands.insert_inventory_sql, (product_id, quantity))
    conn.commit()
    print(f"Inventory for product ID {product_id} inserted successfully.")

def insert_transaction(conn, transaction_id, customer_id, product_id, quantity, date):
    cursor = conn.cursor()
    cursor.execute(sql_commands.insert_transaction_sql, (transaction_id, customer_id, product_id, quantity, date))
    conn.commit()
    print(f"Transaction for customer ID {customer_id} inserted successfully.")

def update_product(conn, product_id, name, supplier_id, buying_price, selling_price):
    cursor = conn.cursor()
    cursor.execute(sql_commands.update_product_sql, (name, supplier_id, buying_price, selling_price, product_id))
    conn.commit()
    print(f"Product with ID {product_id} updated successfully.")

def update_supplier(conn, supplier_id, name, phone_number):
    cursor = conn.cursor()
    cursor.execute(sql_commands.update_supplier_sql, (name, phone_number, supplier_id))
    conn.commit()
    print(f"Supplier with ID {supplier_id} updated successfully.")

def update_customer(conn, customer_id, name, email, total_spent):
    cursor = conn.cursor()
    cursor.execute(sql_commands.update_customer_sql, (name, email, total_spent, customer_id))
    conn.commit()
    print(f"Customer with ID {customer_id} updated successfully.")

def update_discount(conn, discount_id, product_id, discount_percentage, start_date, end_date):
    cursor = conn.cursor()
    cursor.execute(sql_commands.update_discount_sql, (product_id, discount_percentage, start_date, end_date, discount_id))
    conn.commit()
    print(f"Discount with ID {discount_id} updated successfully.")

def update_loyalty_program(conn, loyalty_id, discount_id, points_required):
    cursor = conn.cursor()
    cursor.execute(sql_commands.update_loyalty_program_sql, (discount_id, points_required, loyalty_id))
    conn.commit()
    print(f"Loyalty Program with ID {loyalty_id} updated successfully.")

def update_inventory(conn, product_id, quantity):
    cursor = conn.cursor()
    cursor.execute(sql_commands.update_inventory_sql, (quantity, product_id))
    conn.commit()
    print(f"Inventory for product ID {product_id} updated successfully.")

def update_transaction(conn, transaction_id, customer_id, product_id, quantity, date):
    cursor = conn.cursor()
    cursor.execute(sql_commands.update_transaction_sql, (customer_id, product_id, quantity, date, transaction_id))
    conn.commit()
    print(f"Transaction with ID {transaction_id} updated successfully.")

# Delete Functions
def delete_product(conn, product_id):
    cursor = conn.cursor()
    cursor.execute(sql_commands.delete_product_sql, (product_id,))
    conn.commit()
    print(f"Product with ID {product_id} deleted successfully.")

def delete_supplier(conn, supplier_id):
    cursor = conn.cursor()
    cursor.execute(sql_commands.delete_supplier_sql, (supplier_id,))
    conn.commit()
    print(f"Supplier with ID {supplier_id} deleted successfully.")

def delete_customer(conn, customer_id):
    cursor = conn.cursor()
    cursor.execute(sql_commands.delete_customer_sql, (customer_id,))
    conn.commit()
    print(f"Customer with ID {customer_id} deleted successfully.")

def delete_discount(conn, discount_id):
    cursor = conn.cursor()
    cursor.execute(sql_commands.delete_discount_sql, (discount_id,))
    conn.commit()
    print(f"Discount with ID {discount_id} deleted successfully.")

def delete_loyalty_program(conn, loyalty_id):
    cursor = conn.cursor()
    cursor.execute(sql_commands.delete_loyalty_program_sql, (loyalty_id,))
    conn.commit()
    print(f"Loyalty Program with ID {loyalty_id} deleted successfully.")

def delete_inventory(conn, product_id):
    cursor = conn.cursor()
    cursor.execute(sql_commands.delete_inventory_sql, (product_id,))
    conn.commit()
    print(f"Inventory for product ID {product_id} deleted successfully.")

def delete_transaction(conn, transaction_id):
    cursor = conn.cursor()
    cursor.execute(sql_commands.delete_transaction_sql, (transaction_id,))
    conn.commit()
    print(f"Transaction with ID {transaction_id} deleted successfully.")