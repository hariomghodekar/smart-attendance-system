from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/student-login", methods=["GET", "POST"])
def student_login():

    if request.method == "POST":
        print("Login button clicked")

        roll_number = request.form["roll_number"]
        password = request.form["password"]

        print("Roll Number:", roll_number)
        print("Password:", password)

    return render_template("student_login.html")


if __name__ == "__main__":
    app.run(debug=True)