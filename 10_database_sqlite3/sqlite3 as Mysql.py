import sqlite3


# Function to create a SQLite database and table
def create_database():
    # Connect to a SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()

    # Create a table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            email TEXT NOT NULL
        )
    """
    )

    # Insert some example data
    users_data = [
        ("Alice", 30, "alice@example.com"),
        ("Bob", 25, "bob@example.com"),
        ("Charlie", 35, "charlie@example.com"),
    ]

    cursor.executemany(
        "INSERT INTO users (name, age, email) VALUES (?, ?, ?)", users_data
    )

    # Commit changes and close the connection
    conn.commit()
    conn.close()


# Function to display data in a MySQL-like shell format
def display_data():
    # Connect to the SQLite database
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()

    # Query the database
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    # Display the results in a MySQL shell-like format
    print("+----+---------+-----+-------------------+")
    print("| ID | Name    | Age | Email             |")
    print("+----+---------+-----+-------------------+")
    for row in rows:
        print(f"| {row[0]:<2} | {row[1]:<7} | {row[2]:<3} | {row[3]:<17} |")
    print("+----+---------+-----+-------------------+")

    # Close the connection
    conn.close()


# Main execution
if __name__ == "__main__":
    create_database()
    display_data()
