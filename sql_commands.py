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