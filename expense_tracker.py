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

# === User CRUD ===
def user_menu():
    print("--- User Management ---")
    print("1. Create User")
    print("2. View All Users")
    print("3. Update User")
    print("4. Delete User")
    print("5. Back to Main Menu")
    
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
    print("5. Back to Main Menu")
    
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
    print("5. Back to Main Menu")
    
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

if __name__ == "__main__":
    main_menu()
