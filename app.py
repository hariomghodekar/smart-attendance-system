from flask import Flask, render_template, request
from database import register_student, get_all_students

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/student-login", methods=["GET", "POST"])
def student_login():

    if request.method == "POST":
        roll_number = request.form["roll_number"]
        password = request.form["password"]

        print("Login button clicked")
        print("Roll Number:", roll_number)
        print("Password:", password)

    return render_template("student_login.html")


@app.route("/student-register", methods=["GET", "POST"])
def student_register():

    if request.method == "POST":

        register_student(
            request.form["full_name"],
            request.form["email"],
            request.form["phone"],
            request.form["username"],
            request.form["password"],
            request.form["roll_number"],
            request.form["class_name"]
        )

        return "Student Registered Successfully!"

    return render_template("student_register.html")


@app.route("/students")
def students():

    students = get_all_students()

    return render_template("students.html", students=students)


if __name__ == "__main__":
    app.run(debug=True)