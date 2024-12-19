
# Personal Expense Tracker

This project is a Personal Expense Tracker application designed to manage users, categories, and expenses. The app allows you to create and manage users, categories, and expenses, and supports logging in, registering new users, and performing CRUD (Create, Read, Update, Delete) operations on each of these entities.

## Features

- **User Management:** Add, view, update, and delete users.
- **Category Management:** Add, view, update, and delete categories (e.g., Food, Travel, Utilities).
- **Expense Management:** Create, view, update, and delete expenses associated with users and categories.
- **Login & Registration:** Users can register and log in to access the dashboard.

## Technologies Used

- **Python 3.x**: The backend is built using Python.
- **SQLAlchemy**: ORM used to interact with the SQLite database.
- **SQLite**: Lightweight relational database used to store user, category, and expense data.

### Description of Files

- **models/user.py**: Contains the `User` model, which represents users in the system.
- **models/category.py**: Contains the `Category` model, representing expense categories.
- **models/expense.py**: Contains the `Expense` model, representing user expenses.
- **models/login.py**: Contains the `Login` model, used to authenticate users.
- **base.py**: Contains the SQLAlchemy `Base` class that all models inherit from.
- **main.py**: The main application file with all the logic for user login, registration, and CRUD operations for users, categories, and expenses.
- **README.md**: This file.



## Usage

1. **Login/Register**: Upon running the program, you will be presented with the login screen. You can either log in with an existing account or register a new one.

2. **Dashboard**: After logging in, you will be directed to the user dashboard where you can manage users, categories, and expenses.

3. **User Management**: From the dashboard, you can manage users (create, view, update, delete).

4. **Category Management**: Manage categories for your expenses (create, view, update, delete).

5. **Expense Management**: Create and manage expenses by associating them with a user and a category.

6. **Logout**: To log out and return to the login screen, select the "Logout" option from the dashboard.

## Example

### Login:

```
===== Login =====
Enter username: mary
Enter password: password123
Welcome back, mary!
```

### Dashboard:

```
===== Personal Expense Tracker =====
1. Manage Users
2. Manage Categories
3. Manage Expenses
4. Logout
```

### User Management Menu:

```
--- User Management ---
1. Create User
2. View All Users
3. Update User
4. Delete User
5. Back to Dashboard
```

### Expense Creation:

```
Enter expense amount: 25.5
Enter expense description: Lunch
Enter user ID: 1
Enter category ID: 1
Expense created: Expense(amount=25.5, description='Lunch', user_id=1, category_id=1)
```

## Database

The application uses SQLite as the database, and the tables are automatically created when the application starts if they do not already exist. The following tables are used:

- **User**: Stores user details.
- **Category**: Stores expense categories (e.g., Food, Utilities).
- **Expense**: Stores expense details, including amount, description, and links to users and categories.

## Future Enhancements

- Add the ability to export data (e.g., as CSV or PDF).
- Improve error handling for invalid inputs.
- Add user authentication with hashed passwords (currently, passwords are stored in plain text).
- Implement additional filtering and sorting options for expenses.

## License

This project is open-source and available under the [MIT License](LICENSE).

