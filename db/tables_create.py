from queries_sql import mycon, cursor

#Creating all tables in the database
def create_tables():
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS users
                   (user_id INT AUTO_INCREMENT PRIMARY KEY,
                   username VARCHAR(50),
                   email VARCHAR(100),
                   phone VARCHAR(15),
                   address VARCHAR(225),
                   password VARCHAR(100),
                   user_role VARCHAR(20))
                   """)
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS vehicles
                   (vehicle_no VARCHAR(30) PRIMARY KEY,
                   model VARCHAR(50),
                   type VARCHAR(50),
                   user_id INT,
                   FOREIGN KEY (user_id) REFERENCES users(user_id))
                   """)
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS services
                   (service_type VARCHAR(60) PRIMARY KEY)
                   """)
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS service_bookings
                   (service_id INT AUTO_INCREMENT PRIMARY KEY,
                   vehicle_no VARCHAR(30),
                   service_type VARCHAR(60),
                   booking_date DATE,
                   status VARCHAR(20),
                   FOREIGN KEY (vehicle_no) REFERENCES vehicles(vehicle_no),
                   FOREIGN KEY (service_type) REFERENCES services(service_type))
                   """)
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS mechanics_info
                   (mechanic_id INT AUTO_INCREMENT PRIMARY KEY,
                   mechanic VARCHAR(50))
                   """)
    cursor.execute("""CREATE TABLE IF NOT EXISTS mechanic_assignments
                   (assignment_id INT AUTO_INCREMENT PRIMARY KEY,
                   service_id INT,
                   mechanic_id INT,
                   FOREIGN KEY (service_id) REFERENCES service_bookings(service_id),
                   FOREIGN KEY (mechanic_id) REFERENCES mechanics_info(mechanic_id))
                   """)
    cursor.execute("""CREATE TABLE IF NOT EXISTS invoices
                   (invoice_id INT AUTO_INCREMENT PRIMARY KEY,
                   user_id INT,
                   service_id INT,
                   amount DECIMAL(10, 2),
                   invoice_date DATE,
                   FOREIGN KEY (user_id) REFERENCES users(user_id),
                   FOREIGN KEY (service_id) REFERENCES service_bookings(service_id))
                   """)
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS feedback
                   (feedback_id INT AUTO_INCREMENT PRIMARY KEY,
                   service_id INT,
                   rating INT CHECK (rating BETWEEN 1 AND 5),
                   comments VARCHAR(255),
                   FOREIGN KEY (service_id) REFERENCES service_bookings(service_id))
                   """)
    mycon.commit()

# Inserting data into the table-user
def in_users(username, email, phone, address, password, user_role):
    try:
        cursor.execute("""
                       INSERT INTO users (username, email, phone, address, password, user_role)
                       VALUES (%s, %s, %s, %s, %s, %s)
                       """, (username, email, phone, address, password, user_role))
        mycon.commit()
    except Exception as e:
        print(f"Error inserting user: {e}")
        mycon.rollback()

# Inserting data into the table-vehicles
def in_vehicles(vehicle_no, model, type, user_id):
    try:
        cursor.execute("""
                       INSERT INTO vehicles (vehicle_no, model, type, user_id)
                       VALUES (%s, %s, %s, %s)
                       """, (vehicle_no, model, type, user_id))
        mycon.commit()
    except Exception as e:
        print(f"Error inserting vehicle: {e}")
        mycon.rollback()

# Inserting data into the table-services
def in_services(service_type):
    try:
        cursor.execute("""
                       INSERT INTO services (service_type)
                       VALUES (%s)
                       """, (service_type,))
        mycon.commit()
    except Exception as e:
        print(f"Error inserting service: {e}")
        mycon.rollback()

# Inserting data into the table-service_bookings
def in_service_bookings(vehicle_no, service_type, booking_date, status):
    try:
        cursor.execute("""
                       INSERT INTO service_bookings (vehicle_no, service_type, booking_date, status)
                       VALUES (%s, %s, %s, %s)
                       """, (vehicle_no, service_type, booking_date, status))
        mycon.commit()
    except Exception as e:
        print(f"Error inserting service booking: {e}")
        mycon.rollback()

# Inserting data into the table-mechanics_info
def in_mechanics(mechanic):
    try:
        cursor.execute("""
                       INSERT INTO mechanics_info (mechanic)
                       VALUES (%s)
                       """, (mechanic,))
        mycon.commit()
    except Exception as e:
        print(f"Error inserting mechanic: {e}")
        mycon.rollback()

# Inserting data into the table-mechanic_assignments
def in_mechanic_assignments(service_id, mechanic_id):
    try:
        cursor.execute("""
                       INSERT INTO mechanic_assignments (service_id, mechanic_id)
                       VALUES (%s, %s)
                       """, (service_id, mechanic_id))
        mycon.commit()
    except Exception as e:
        print(f"Error inserting mechanic assignment: {e}")
        mycon.rollback()

# Inserting data into the table-invoices
def in_invoices(user_id, service_id, amount, invoice_date):
    try:
        cursor.execute("""
                       INSERT INTO invoices (user_id, service_id, amount, invoice_date)
                       VALUES (%s, %s, %s, %s)
                       """, (user_id, service_id, amount, invoice_date))
        mycon.commit()
    except Exception as e:
        print(f"Error inserting invoice: {e}")
        mycon.rollback()

# Inserting data into the table-feedback
def in_feedback(service_id, rating, comments):
    try:
        cursor.execute("""
                       INSERT INTO feedback (service_id, rating, comments)
                       VALUES (%s, %s, %s)
                       """, (service_id, rating, comments))
        mycon.commit()
    except Exception as e:
        print(f"Error inserting feedback: {e}")
        mycon.rollback()