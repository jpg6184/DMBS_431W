CREATE TABLE Product (
            product_id INT,
            name VARCHAR(100) NOT NULL,
            supplier_id INT,
            buying_price DECIMAL(10, 2),
            selling_price DECIMAL(10, 2),
            PRIMARY KEY (product_id)
        );

CREATE TABLE Supplier (
            supplier_id INT,
            name VARCHAR(100) NOT NULL,
            phone_number VARCHAR(15),
            PRIMARY KEY (supplier_id)
        );


CREATE TABLE Customer (
            customer_id INT,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100),
            total_spent DECIMAL(10, 2),
            PRIMARY KEY (customer_id)
        );

CREATE TABLE Discount (
            discount_id INT,
            product_id INT,
            discount_percentage DECIMAL(5, 2),
            start_date DATE NOT NULL,
            end_date DATE NOT NULL,
            PRIMARY KEY (discount_id),      
            FOREIGN KEY (product_id) REFERENCES Product(product_id)
        );

CREATE TABLE LoyaltyProgram (
            loyalty_id INT, 
            discount_id INT, 
            points_required INT,  
            PRIMARY KEY (loyalty_id), 
            FOREIGN KEY (discount_id) REFERENCES Discount(discount_id)
        );

CREATE TABLE Inventory (
            product_id INT,
            quantity INT NOT NULL,
            PRIMARY KEY (product_id),
            FOREIGN KEY (product_id) REFERENCES Product(product_id)
        );

CREATE TABLE Transaction (
            transaction_id INT,
            customer_id INT,
            product_id INT,
            quantity INT NOT NULL,
            date DATE NOT NULL,
            PRIMARY KEY (transaction_id),
            FOREIGN KEY (customer_id) REFERENCES Customer(customer_id),
            FOREIGN KEY (product_id) REFERENCES Product(product_id)
);




