insert_product_sql = """
    INSERT INTO Product (product_id, name, supplier_id, buying_price, selling_price)
    VALUES (%s, %s, %s, %s, %s);
"""

insert_supplier_sql = """
    INSERT INTO Supplier (supplier_id, name, phone_number)
    VALUES (%s, %s, %s);
"""

insert_customer_sql = """
    INSERT INTO Customer (customer_id, name, email)
    VALUES (%s, %s, %s);
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
    FROM 
        Product p
    JOIN 
        Supplier s ON p.supplier_id = s.supplier_id
    ORDER BY   
        s.name, p.product_id;
"""

view_suppliers_sql = """
    SELECT supplier_id, name, phone_number
    FROM Supplier;
"""


view_transactions_sql = """
    SELECT transaction_id, customer_id, product_id, date
    FROM Transaction;
"""

view_transactions_by_customer = """
    SELECT
        c.name AS customer_name,
        p.name AS product_name,
        SUM(t.quantity * p.selling_price) AS total_price
    FROM
        Transaction t
    JOIN
        Customer c ON t.customer_id = c.customer_id
    JOIN
        Product p ON t.product_id = p.product_id
    GROUP BY
        c.customer_id, p.product_id
    ORDER BY
        c.name, p.name;
"""

view_low_stock = """
    SELECT 
        p.name AS product_name,
        i.quantity AS stock_quantity
    FROM 
        Inventory i
    JOIN 
        Product p ON i.product_id = p.product_id
    WHERE 
        i.quantity < 10
    ORDER BY 
        i.quantity ASC;
"""

view_product_by_revenue = """
    SELECT 
        p.name AS product_name,
        SUM(t.quantity) AS total_quantity_sold,
        SUM(t.quantity * p.selling_price) AS total_revenue
    FROM 
        Transaction t
    JOIN 
        Product p ON t.product_id = p.product_id
    GROUP BY 
        p.product_id
    ORDER BY 
        total_revenue DESC;
"""

view_employee_by_sales = """
    SELECT 
        e.name AS employee_name,
        COUNT(t.transaction_id) AS total_transactions,
        SUM(t.quantity * p.selling_price) AS total_sales
    FROM 
        Transaction t
    JOIN 
        Employee e ON t.employee_id = e.employee_id
    JOIN 
        Product p ON t.product_id = p.product_id
    GROUP BY 
        e.employee_id
    ORDER BY 
        total_sales DESC;
"""

view_transaction_count_by_customer = """
    SELECT 
        c.name AS customer_name,
        COUNT(DISTINCT t.transaction_id) AS total_purchases
    FROM 
        Customer c
    JOIN 
        Transaction t ON c.customer_id = t.customer_id
    GROUP BY 
        c.customer_id
    ORDER BY 
        total_purchases DESC;
"""

view_profit_margins = """
    SELECT 
        p.name AS product_name,
        p.selling_price - p.buying_price AS profit_margin,
        (p.selling_price - p.buying_price) / p.selling_price * 100 AS profit_margin_percentage
    FROM 
        Product p
    ORDER BY 
        profit_margin_percentage DESC;
"""

view_highest_discounts = """
    SELECT 
        p.name AS product_name,
        AVG(d.discount_percentage) AS avg_discount
    FROM 
        Discount d
    JOIN 
        Product p ON d.product_id = p.product_id
    GROUP BY 
        p.product_id
    ORDER BY 
        avg_discount DESC
    LIMIT 10;

"""

view_customers_by_spending = """
    SELECT 
        c.name AS customer_name,
        SUM(t.quantity * p.selling_price) AS total_spent
    FROM 
        Customer c
    JOIN 
        Transaction t ON c.customer_id = t.customer_id
    JOIN 
        Product p ON t.product_id = p.product_id
    GROUP BY 
        c.customer_id
    ORDER BY 
        total_spent DESC
    LIMIT 10;
"""
view_inventory_value = """
    SELECT 
        p.name AS product_name,
        i.quantity AS stock_quantity,
        i.quantity * p.buying_price AS inventory_value
    FROM 
        Product p
    JOIN 
        Inventory i ON p.product_id = i.product_id
    ORDER BY 
        inventory_value DESC;
"""