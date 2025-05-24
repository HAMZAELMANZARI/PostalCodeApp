# Postal Code Management Application

A command-line application designed to manage postal codes using SQLite. This tool allows users to add, view, update, and delete postal code entries efficiently.

## Features

- **Add Postal Code**: Store a postal code with a user ID, city name, and postal code number.
- **View Postal Codes**: Display all entries in the database.
- **Update Entries**: Modify existing city names or postal codes using the user ID.
- **Delete Entries**: Remove entries by specifying the user ID.
- **Exit**: Safely close the database connection and exit the application.

## Prerequisites

- Python 3.x
- `sqlite3` module (included in Python's standard library)

## Installation

1. **Clone the repository** (if applicable) or create a new directory for the project.
2. **Create a database directory**:
   ```bash
   mkdir database
   ```
   This ensures the `postal_code.db` file is stored correctly.

## Usage

1. **Run the script**:
   ```bash
   python app.py
   ```
2. **Menu Options**:
   ```
   Welcome to Postal Code App

   1. Add Postal Code.
   2. View Postal Code.
   3. Update Postal Code.
   4. Delete Postal Code.
   5. Exit.
   ```
   Enter the number corresponding to your desired action.

### Example Workflow

- **Add a Postal Code**:
  ```
  Choose one number: 1
  Enter User ID: 5       (Must be a single character, e.g., "A", "1")
  Enter City Name: Paris
  Enter Postal Code: 75000
  ```
  Successfully adds the entry to the database.

- **View Entries**:
  ```
  Choose one number: 2
  User ID: 5 | City Name: Paris | Postal Code: 75000
  ```

- **Update an Entry**:
  ```
  Choose one number: 3
  Enter User ID: 5
  Enter New City: Lyon
  Enter New Postal Code: 69000
  ```

- **Delete an Entry**:
  ```
  Choose one number: 4
  Enter User ID: 5
  ```

## Notes/Limitations

- **User ID Restriction**: The `user_id` must be a **single character** (e.g., "A", "7"). Longer inputs will be rejected.
- **Postal Code Validation**: The application does not validate postal code formats. Ensure inputs are numeric to avoid errors.
- **Database Path**: The database is created in `database/postal_code.db`. Ensure the `database` directory exists before running the app.

---

Feel free to contribute or report issues! 🚀