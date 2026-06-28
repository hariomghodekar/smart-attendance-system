import sqlite3


def get_connection():
    return sqlite3.connect("database.db")


def create_tables():
    connection = get_connection()
    cursor = connection.cursor()

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

    connection.commit()
    connection.close()

    print("Institution table created successfully!")


if __name__ == "__main__":
    create_tables()