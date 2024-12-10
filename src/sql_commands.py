insert_product_sql = """
    INSERT INTO Product (product_id, name, supplier_id, buying_price, selling_price)
    VALUES (%s, %s, %s, %s, %s);
"""

insert_supplier_sql = """
    INSERT INTO Supplier (supplier_id, name, phone_number)
    VALUES (%s, %s, %s);
"""

insert_customer_sql = """
    INSERT INTO Customer (customer_id, name, email, total_spent)
    VALUES (%s, %s, %s, %s);
"""

insert_discount_sql = """
    INSERT INTO Discount (discount_id, product_id, discount_percentage, start_date, end_date)
    VALUES (%s, %s, %s, %s, %s);
"""

insert_loyalty_program_sql = """
    INSERT INTO LoyaltyProgram (loyalty_id, discount_id, points_required)
    VALUES (%s, %s, %s);
"""

insert_inventory_sql = """
    INSERT INTO Inventory (product_id, quantity)
    VALUES (%s, %s);
"""

insert_transaction_sql = """
    INSERT INTO Transaction (transaction_id, customer_id, product_id, quantity, date)
    VALUES (%s, %s, %s, %s, %s);
"""

insert_employee_sql = """
    INSERT INTO Employee (employee_id, name)
    VALUES (%s, %s);
    """

insert_user_sql = """
    INSERT INTO Users (username, hashed_password, role)
    VALUES (%s, %s, %s);
    """

update_product_sql = """
    UPDATE Product
    SET name = %s, supplier_id = %s, buying_price = %s, selling_price = %s
    WHERE product_id = %s;
"""

update_supplier_sql = """
    UPDATE Supplier
    SET name = %s, phone_number = %s
    WHERE supplier_id = %s;
"""

update_customer_sql = """
    UPDATE Customer
    SET name = %s, email = %s, total_spent = %s
    WHERE customer_id = %s;
"""

update_discount_sql = """
    UPDATE Discount
    SET product_id = %s, discount_percentage = %s, start_date = %s, end_date = %s
    WHERE discount_id = %s;
"""

update_loyalty_program_sql = """
    UPDATE LoyaltyProgram
    SET discount_id = %s, points_required = %s
    WHERE loyalty_id = %s;
"""

update_inventory_sql = """
    UPDATE Inventory
    SET quantity = %s
    WHERE product_id = %s;
"""

update_transaction_sql = """
    UPDATE Transaction
    SET customer_id = %s, product_id = %s, quantity = %s, date = %s
    WHERE transaction_id = %s;
"""

update_employee_sql = """
    UPDATE Employee
    SET name = %s
    WHERE employee_id = %s
"""

delete_product_sql = """
    DELETE FROM Product
    WHERE product_id = %s;
"""

delete_supplier_sql = """
    DELETE FROM Supplier
    WHERE supplier_id = %s;
"""

delete_customer_sql = """
    DELETE FROM Customer
    WHERE customer_id = %s;
"""

delete_discount_sql = """
    DELETE FROM Discount
    WHERE discount_id = %s;
"""

delete_loyalty_program_sql = """
    DELETE FROM LoyaltyProgram
    WHERE loyalty_id = %s;
"""

delete_inventory_sql = """
    DELETE FROM Inventory
    WHERE product_id = %s;
"""

delete_transaction_sql = """
    DELETE FROM Transaction
    WHERE transaction_id = %s;
"""

delete_employee_sql = """
    DELETE FROM Employee
    WHERE employee_id = %s;
"""

view_products_sql = """
    SELECT product_id, name, supplier_id, buying_price, selling_price
    FROM Product;
"""

view_products_by_supplier_sql = """
    SELECT p.product_id, p.name AS product_name, s.name AS supplier_name, p.buying_price, p.selling_price
    FROM Product p
    JOIN Supplier s ON p.supplier_id = s.supplier_id
    ORDER BY s.name, p.product_id;
"""

view_suppliers_sql = """
    SELECT supplier_id, name, phone_number
    FROM Supplier;
"""


view_transactions_sql = """
    SELECT transaction_id, customer_id, product_id, date
    FROM Transaction;
"""
