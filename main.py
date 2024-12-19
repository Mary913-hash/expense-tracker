import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.user import User, Base
from models.category import Category
from models.expense import Expense

# Set up the database engine and session
engine = create_engine('sqlite:///expense_tracker.db')
Base.metadata.create_all(engine)  # Create tables
Session = sessionmaker(bind=engine)
session = Session()

def main_menu():
    print("===== Personal Expense Tracker =====")
    print("1. Manage Users")
    print("2. Manage Categories")
    print("3. Manage Expenses")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        user_menu()
    elif choice == '2':
        category_menu()
    elif choice == '3':
        expense_menu()
    elif choice == '4':
        sys.exit()
    else:
        print("Invalid choice. Try again.")
        main_menu()

def user_menu():
    print("--- User Management ---")
    print("1. Create User")
    print("2. View All Users")
    print("3. Back to Main Menu")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        create_user()
    elif choice == '2':
        view_users()
    elif choice == '3':
        main_menu()
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

def category_menu():
    print("--- Category Management ---")
    print("1. Create Category")
    print("2. View All Categories")
    print("3. Back to Main Menu")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        create_category()
    elif choice == '2':
        view_categories()
    elif choice == '3':
        main_menu()
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

def expense_menu():
    print("--- Expense Management ---")
    print("1. Create Expense")
    print("2. View All Expenses")
    print("3. Back to Main Menu")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        create_expense()
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        main_menu()
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

if __name__ == "__main__":
    main_menu()
