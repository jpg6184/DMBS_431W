CREATE TABLE Supplier (
            supplier_id INT,
            name VARCHAR(100) NOT NULL,
            phone_number VARCHAR(15),
            PRIMARY KEY (supplier_id)
);
CREATE TABLE Product (
            product_id INT,
            name VARCHAR(100) NOT NULL,
            supplier_id INT,
            buying_price DECIMAL(10, 2),
            selling_price DECIMAL(10, 2),
            PRIMARY KEY (product_id),
            FOREIGN KEY (supplier_id) REFERENCES Supplier(supplier_id)
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

CREATE TABLE Employee (
            employee_id INT, 
            name VARCHAR(100) NOT NULL,
            PRIMARY KEY (employee_id)      
);

CREATE TABLE Transaction (
            transaction_id INT,
            customer_id INT,
            employee_id INT, 
            product_id INT,
            quantity INT NOT NULL,
            date DATE NOT NULL,
            PRIMARY KEY (transaction_id),
            FOREIGN KEY (customer_id) REFERENCES Customer(customer_id),
            FOREIGN KEY (product_id) REFERENCES Product(product_id),
            FOREIGN KEY (employee_id) REFERENCES Employee(employee_id)
);

CREATE TABLE Users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255) NOT NULL UNIQUE,
            hashed_password VARCHAR(255) NOT NULL,
            role VARCHAR(50) NOT NULL DEFAULT 'guest',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);




