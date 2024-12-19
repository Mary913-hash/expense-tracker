import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.user import User, Base
from models.category import Category
from models.expense import Expense
from models.login import Login
from base import Base  # Shared Base for all models

# Set up the database engine and session
engine = create_engine('sqlite:///expense_tracker.db')
Base.metadata.create_all(engine)  # Create tables if they don't exist
Session = sessionmaker(bind=engine)
session = Session()

# Global variable to keep track of the logged-in user
logged_in_user = None

# Function to handle user login
def login_menu():
    global logged_in_user
    print("\n===== Login =====")
    username = input("Enter username: ")
    password = input("Enter password: ")

    user = session.query(Login).filter_by(username=username, password=password).first()
    if user:
        logged_in_user = user
        print(f"Welcome back, {username}!")
        user_dashboard()
    else:
        print("Invalid username or password. Please try again.")

# Function to handle user registration
def register_menu():
    print("\n===== Register =====")
    username = input("Enter username: ")
    password = input("Enter password: ")

    existing_user = session.query(Login).filter_by(username=username).first()
    if existing_user:
        print("Username already exists. Please choose a different username.")
    else:
        new_user = Login(username=username, password=password)
        session.add(new_user)
        session.commit()
        print("Registration successful! You can now log in.")

# Function for the user's dashboard
def user_dashboard():
    while True:
        print("\n===== Personal Expense Tracker =====")
        print("1. Manage Users")
        print("2. Manage Categories")
        print("3. Manage Expenses")
        print("4. Logout")

        choice = input("Enter your choice: ")

        if choice == '1':
            user_menu()  # Directing to user management menu
        elif choice == '2':
            category_menu()  # Directing to category management menu
        elif choice == '3':
            expense_menu()  # Directing to expense management menu
        elif choice == '4':
            print("Logging out...")
            global logged_in_user
            logged_in_user = None
            break  # Exit the dashboard and go back to the main menu
        else:
            print("Invalid choice. Please try again.")

# === User CRUD ===
def user_menu():
    print("--- User Management ---")
    print("1. Create User")
    print("2. View All Users")
    print("3. Update User")
    print("4. Delete User")
    print("5. Back to Dashboard")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        create_user()
    elif choice == '2':
        view_users()
    elif choice == '3':
        update_user()
    elif choice == '4':
        delete_user()
    elif choice == '5':
        user_dashboard()  # Go back to the dashboard
    else:
        print("Invalid choice. Try again.")
        user_menu()

def create_user():
    name = input("Enter user name: ")
    user = User(name=name)
    session.add(user)
    session.commit()
    print(f"User '{name}' created successfully!")

def view_users():
    users = session.query(User).all()
    for user in users:
        print(user)

def update_user():
    user_id = int(input("Enter the user ID to update: "))
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        user.name = input("Enter new name: ") or user.name
        session.commit()
        print(f"User {user_id} updated successfully!")
    else:
        print("User not found.")

def delete_user():
    user_id = int(input("Enter the user ID to delete: "))
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        session.delete(user)
        session.commit()
        print(f"User {user_id} deleted successfully!")
    else:
        print("User not found.")

# === Category CRUD ===
def category_menu():
    print("--- Category Management ---")
    print("1. Create Category")
    print("2. View All Categories")
    print("3. Update Category")
    print("4. Delete Category")
    print("5. Back to Dashboard")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        create_category()
    elif choice == '2':
        view_categories()
    elif choice == '3':
        update_category()
    elif choice == '4':
        delete_category()
    elif choice == '5':
        user_dashboard()  # Go back to the dashboard
    else:
        print("Invalid choice. Try again.")
        category_menu()

def create_category():
    name = input("Enter category name: ")
    category = Category(name=name)
    session.add(category)
    session.commit()
    print(f"Category '{name}' created successfully!")

def view_categories():
    categories = session.query(Category).all()
    for category in categories:
        print(category)

def update_category():
    category_id = int(input("Enter the category ID to update: "))
    category = session.query(Category).filter_by(id=category_id).first()
    if category:
        category.name = input("Enter new category name: ") or category.name
        session.commit()
        print(f"Category {category_id} updated successfully!")
    else:
        print("Category not found.")

def delete_category():
    category_id = int(input("Enter the category ID to delete: "))
    category = session.query(Category).filter_by(id=category_id).first()
    if category:
        session.delete(category)
        session.commit()
        print(f"Category {category_id} deleted successfully!")
    else:
        print("Category not found.")

# === Expense CRUD ===
def expense_menu():
    print("--- Expense Management ---")
    print("1. Create Expense")
    print("2. View All Expenses")
    print("3. Update Expense")
    print("4. Delete Expense")
    print("5. Back to Dashboard")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        create_expense()
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        update_expense()
    elif choice == '4':
        delete_expense()
    elif choice == '5':
        user_dashboard()  # Go back to the dashboard
    else:
        print("Invalid choice. Try again.")
        expense_menu()

def create_expense():
    try:
        amount = float(input("Enter expense amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return create_expense()

    description = input("Enter expense description: ")
    try:
        user_id = int(input("Enter user ID: "))
        category_id = int(input("Enter category ID: "))
    except ValueError:
        print("Invalid ID. Please enter an integer.")
        return create_expense()

    expense = Expense(amount=amount, description=description, user_id=user_id, category_id=category_id)
    session.add(expense)
    session.commit()
    print(f"Expense created: {expense}")

def view_expenses():
    expenses = session.query(Expense).all()
    for expense in expenses:
        print(expense)

def update_expense():
    expense_id = int(input("Enter the expense ID to update: "))
    expense = session.query(Expense).filter_by(id=expense_id).first()
    if expense:
        try:
            expense.amount = float(input("Enter new amount (leave blank to keep current): ") or expense.amount)
        except ValueError:
            print("Invalid input. Keeping existing amount.")
        expense.description = input("Enter new description: ") or expense.description
        session.commit()
        print(f"Expense {expense_id} updated successfully!")
    else:
        print("Expense not found.")

def delete_expense():
    expense_id = int(input("Enter the expense ID to delete: "))
    expense = session.query(Expense).filter_by(id=expense_id).first()
    if expense:
        session.delete(expense)
        session.commit()
        print(f"Expense {expense_id} deleted successfully!")
    else:
        print("Expense not found.")

# Function to handle the main menu (Login/Registration)
def main_menu():
    while True:
        print("\n===== Personal Expense Tracker =====")
        print("1. Login")
        print("2. Register")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            login_menu()
        elif choice == '2':
            register_menu()
        elif choice == '3':
            print("Exiting... Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

# Call the main menu
if __name__ == "__main__":
    main_menu()
