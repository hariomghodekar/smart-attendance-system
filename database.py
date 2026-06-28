import sqlite3


def get_connection():
    return sqlite3.connect("database.db")


def create_tables():
    connection = get_connection()
    cursor = connection.cursor()

    # Institution Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS institution (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        institution_type TEXT NOT NULL,
        country TEXT NOT NULL,
        state TEXT NOT NULL,
        city TEXT NOT NULL,
        address TEXT,
        postal_code TEXT,
        academic_session TEXT NOT NULL,
        use_department INTEGER DEFAULT 0,
        use_semester INTEGER DEFAULT 0,
        use_section INTEGER DEFAULT 1,
        working_days TEXT NOT NULL
    )
    """)

    # Accounts Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS accounts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        institution_id INTEGER NOT NULL,
        full_name TEXT NOT NULL,
        email TEXT UNIQUE,
        phone TEXT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL,
        profile_photo TEXT,
        is_active INTEGER DEFAULT 1,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (institution_id) REFERENCES institution(id)
    )
    """)

    # Students Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        account_id INTEGER NOT NULL,
        roll_number TEXT,
        admission_number TEXT,
        class_name TEXT NOT NULL,
        section TEXT,
        department TEXT,
        semester TEXT,
        batch TEXT,
        date_of_birth TEXT,
        gender TEXT,
        blood_group TEXT,
        parent_name TEXT,
        parent_phone TEXT,
        emergency_contact TEXT,
        address TEXT,
        FOREIGN KEY (account_id) REFERENCES accounts(id)
    )
    """)

    # Teachers Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS teachers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        account_id INTEGER NOT NULL,
        employee_id TEXT UNIQUE,
        department TEXT,
        designation TEXT,
        qualification TEXT,
        joining_date TEXT,
        FOREIGN KEY (account_id) REFERENCES accounts(id)
    )
    """)

    # Admins Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS admins (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        account_id INTEGER NOT NULL,
        designation TEXT,
        FOREIGN KEY (account_id) REFERENCES accounts(id)
    )
    """)

    connection.commit()
    connection.close()

    print("All tables created successfully!")


if __name__ == "__main__":
    create_tables()