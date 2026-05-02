import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        # Replace with your database credentials
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='supershopmanagement'
        )

        if connection.is_connected():
            print("Successfully connected to the database")
            return connection

    except Error as e:
        print(f"Error: '{e}' occurred")
        return None

def close_connection(connection):
    if connection and connection.is_connected():
        connection.close()
        print("Database connection closed")

def insert_customer(connection, name, contact, address, membership):
    try:
        cursor = connection.cursor()
        query = """
        INSERT INTO Customer (Name, ContactInfo, Address, MembershipStatus)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (name, contact, address, membership))
        connection.commit()  # Save the changes
        print(f"Customer '{name}' added successfully!")
    except Error as e:
        print(f"Error: '{e}' occurred")

def show_all_customers(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Customer")
        customers = cursor.fetchall()
        if customers:
            for customer in customers:
                print(customer)
        else:
            print("No customers found.")
    except Error as e:
        print(f"Error: '{e}' occurred")

def show_customer_by_id(connection, customer_id):
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM Customer WHERE CustomerID = %s"
        cursor.execute(query, (customer_id,))
        customer = cursor.fetchone()
        if customer:
            print(customer)
        else:
            print(f"Customer with ID {customer_id} not found.")
    except Error as e:
        print(f"Error: '{e}' occurred")

def update_customer(connection, customer_id, new_name, new_contact, new_address, new_membership):
    try:
        cursor = connection.cursor()
        query = """
        UPDATE Customer 
        SET Name = %s, ContactInfo = %s, Address = %s, MembershipStatus = %s
        WHERE CustomerID = %s
        """
        cursor.execute(query, (new_name, new_contact, new_address, new_membership, customer_id))
        connection.commit()
        print(f"Customer ID {customer_id} updated successfully!")
    except Error as e:
        print(f"Error: '{e}' occurred")

def delete_customer(connection, customer_id):
    try:
        cursor = connection.cursor()
        query = "DELETE FROM Customer WHERE CustomerID = %s"
        cursor.execute(query, (customer_id,))
        connection.commit()
        print(f"Customer ID {customer_id} deleted successfully!")
    except Error as e:
        print(f"Error: '{e}' occurred")

def show_all_products(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT ProductID, Name, Category, Price, QuantityInStock FROM Product")
        products = cursor.fetchall()
        if products:
            print("\nList of Products:")
            print(f"{'ID':<5}{'Name':<20}{'Category':<15}{'Price':<10}{'Quantity':<10}")
            for product in products:
                print(f"{product[0]:<5}{product[1]:<20}{product[2]:<15}{product[3]:<10}{product[4]:<10}")
        else:
            print("No products found.")
    except Error as e:
        print(f"Error: '{e}' occurred")


if __name__ == "__main__":
    conn = create_connection()
    
    if conn:
        while True:
            print("\nChoose an operation:")
            print("1. Show all customers")
            print("2. Show a customer by ID")
            print("3. Add a new customer")
            print("4. Update a customer")
            print("5. Delete a customer")
            print("6. Show all products and quantities")
            print("7. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                show_all_customers(conn)
            elif choice == "2":
                customer_id = int(input("Enter the Customer ID: "))
                show_customer_by_id(conn, customer_id)
            elif choice == "3":
                name = input("Enter customer name: ")
                contact = input("Enter contact info: ")
                address = input("Enter address: ")
                membership = input("Enter membership status (Regular or Premium): ")
                insert_customer(conn, name, contact, address, membership)
            elif choice == "4":
                customer_id = int(input("Enter the Customer ID to update: "))
                new_name = input("Enter new name: ")
                new_contact = input("Enter new contact info: ")
                new_address = input("Enter new address: ")
                new_membership = input("Enter new membership status (Regular or Premium): ")
                update_customer(conn, customer_id, new_name, new_contact, new_address, new_membership)
            elif choice == "5":
                customer_id = int(input("Enter the Customer ID to delete: "))
                delete_customer(conn, customer_id)
            elif choice == "6":
                show_all_products(conn)
            elif choice == "7":
                close_connection(conn)
                break
            else:
                print("Invalid choice! Please try again.")
