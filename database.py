import sqlite3


def get_connection():
    return sqlite3.connect("database.db")


def create_tables():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS institution(
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

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS accounts(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        institution_id INTEGER,
        full_name TEXT NOT NULL,
        email TEXT UNIQUE,
        phone TEXT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL,
        profile_photo TEXT,
        is_active INTEGER DEFAULT 1,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(
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
        FOREIGN KEY(account_id) REFERENCES accounts(id)
    )
    """)

    connection.commit()
    connection.close()


def register_student(full_name, email, phone, username, password, roll_number, class_name):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO accounts
    (full_name,email,phone,username,password,role)
    VALUES(?,?,?,?,?,?)
    """, (full_name, email, phone, username, password, "Student"))

    account_id = cursor.lastrowid

    cursor.execute("""
    INSERT INTO students
    (account_id,roll_number,class_name)
    VALUES(?,?,?)
    """, (account_id, roll_number, class_name))

    connection.commit()
    connection.close()


def get_all_students():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    SELECT
    students.roll_number,
    accounts.full_name,
    accounts.username,
    students.class_name
    FROM students
    INNER JOIN accounts
    ON students.account_id=accounts.id
    """)

    students = cursor.fetchall()

    connection.close()

    return students


def get_dashboard_statistics():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM students")
    total_students = cursor.fetchone()[0]

    cursor.execute("""
    SELECT COUNT(*)
    FROM accounts
    WHERE role='Teacher'
    """)
    total_teachers = cursor.fetchone()[0]

    connection.close()

    return {
        "students": total_students,
        "teachers": total_teachers
    }


if __name__ == "__main__":
    create_tables()