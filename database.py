import mysql.connector
import bcrypt
from exceptions import *

class Database:

    # Used as a helper method to hash passwords before placing them into the database
    def hash_password(password: str) -> str:
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


    def valid_email(email: str) -> bool:
        try:
            at_index = email.index("@") 
            if at_index > 0 and email.index(".") > at_index:
                return True
        except Exception:
            return False

    @staticmethod
    def create_database():
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="DataBeta176"
        )

        cursor = db.cursor()

        try:
            cursor.execute("CREATE DATABASE IF NOT EXISTS waddlewise_db")
        except:
            print("Something bad happened when creating the database")
            cursor.close()
            db.close()
            return

        cursor.close()
        db.close()

        db = mysql.connector.connect(
            host="localhost",
            user="root", 
            password="DataBeta176",
            database="waddlewise_db"
        )

        cursor = db.cursor()

        # Creating Users Table
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    user_id INT AUTO_INCREMENT PRIMARY KEY,
                    first_name VARCHAR(50) NOT NULL,
                    last_name VARCHAR(50) NOT NULL,
                    email VARCHAR(50) UNIQUE NOT NULL,
                    username VARCHAR(50) UNIQUE NOT NULL,
                    password_hash VARCHAR(255) NOT NULL
                );
            """)
            print("Created users table")    
        except:
            print("Something went wrong when creating the users table")


        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS tasks (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    user_id INT NOT NULL,
                    task_description TEXT NOT NULL,
                    completed BOOLEAN DEFAULT FALSE,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
                );
            """)
            print("Created tasks table")
        except:
            print("Something went wrong when creating the tasks table")


        cursor.close()
        db.close()

    # Used to create a user and enter them into the database, 
    # assuming that all fields are valid.
    @staticmethod
    def create_user(first_name: str, last_name: str, email: str, user: str, password: str, confirm_password: str):
        
        # Raise error if first name is blank or null
        if first_name == "" or first_name is None or first_name.isspace():
            raise InvalidNameError("Invalid first name.")
        
        # Raise error is last name is blank or null
        if last_name == "" or last_name is None or last_name.isspace():
            raise InvalidNameError("Invalid last name.")
        
        # Raise error if email is invalid
        if not Database.valid_email(email):
            raise InvalidEmailError("Invalid email.")

        # Raise error if username is blank or null
        if user == "" or user is None or user.isspace():
            raise InvalidUsernameError("Invalid Username.")
        
        # Raise error if password is blank or null
        if password == "" or password is None or password.isspace():
            raise InvalidPasswordError("You must enter a valid password.")
        
        # Raise error if password is too short (less than 5 characters)
        if len(password) < 5:
            raise InvalidPasswordError("Password must be at least 5 characters long.")
        
        # Raise error if password and confirmed password do not match.
        if password != confirm_password:
            raise NonMatchingPasswordError("Passwords do not match.")

        # Connect to db    
        try:
            db = mysql.connector.connect(
                host="localhost",
                user="root", 
                password="DataBeta176",
                database="waddlewise_db"
            )
        # Handling connection failure
        except:
            print("Could not connect to database")

        cursor = db.cursor()

        hashed_password = Database.hash_password(password)

        try:
            query = "INSERT INTO users (first_name, last_name, email, username, password_hash) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (first_name, last_name, email, user, hashed_password))
            db.commit()
        except mysql.connector.IntegrityError:
            raise UserAlreadyExistsError("User already exists.")
        
    @staticmethod
    def authenticate(key: str, password: str):
        try:
            db = mysql.connector.connect(
                host="localhost",
                user="root", 
                password="DataBeta176",
                database="waddlewise_db"
            )
        except:
            print("Could not connect to database")

        if key == "" or key is None or key.isspace():
            raise InvalidUsernameError("Please enter a valid username or email.")
        
        if password == "" or password is None or password.isspace():
            raise InvalidPasswordError("Please enter a valid password.")
        
        if Database.valid_email(key):
            query = "SELECT password_hash FROM users WHERE email = %s"
        else:
            query = "SELECT password_hash FROM users WHERE username = %s"

        cursor = db.cursor()
        cursor.execute(query, (key,))
        user = cursor.fetchone()
        if user is None:
            raise AuthenticationError("Username not found")
        
        stored_password = user[0]
        if not bcrypt.checkpw(password.encode(), stored_password.encode()):
            raise AuthenticationError("Incorrect password.")
        
        return True


# Run if new columns must be added    
# Database.create_database()

