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
                   user_Role VARCHAR(20))
                   """)
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS vehicles
                   (vehicle_no INT AUTO_INCREMENT PRIMARY KEY,
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
                   vehicle_no INT,
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
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS feedback
                   (feedback_id INT AUTO_INCREMENT PRIMARY KEY,
                   service_id INT,
                   rating INT CHECK (rating BETWEEN 1 AND 5),
                   comments VARCHAR(255),
                   FOREIGN KEY (service_id) REFERENCES service_bookings(service_id))
                   """)
    mycon.commit()

#Closing the connection
mycon.close()