from extensions import db


class Account(db.Model):

    __tablename__ = "accounts"

    id = db.Column(db.Integer, primary_key=True)

    institution_id = db.Column(db.Integer)

    full_name = db.Column(db.String(150), nullable=False)

    email = db.Column(db.String(150), unique=True)

    phone = db.Column(db.String(20))

    username = db.Column(db.String(100), unique=True, nullable=False)

    password = db.Column(db.String(255), nullable=False)

    role = db.Column(db.String(50), nullable=False)

    profile_photo = db.Column(db.String(255))

    is_active = db.Column(db.Boolean, default=True)

    created_at = db.Column(db.DateTime, server_default=db.func.now())


class Student(db.Model):

    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)

    account_id = db.Column(
        db.Integer,
        db.ForeignKey("accounts.id"),
        nullable=False
    )

    roll_number = db.Column(db.String(50))

    admission_number = db.Column(db.String(50))

    class_name = db.Column(db.String(100), nullable=False)

    section = db.Column(db.String(50))

    department = db.Column(db.String(100))

    semester = db.Column(db.String(50))

    batch = db.Column(db.String(50))

    date_of_birth = db.Column(db.String(30))

    gender = db.Column(db.String(20))

    blood_group = db.Column(db.String(10))

    parent_name = db.Column(db.String(150))

    parent_phone = db.Column(db.String(20))

    emergency_contact = db.Column(db.String(20))

    address = db.Column(db.Text)