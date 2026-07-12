from flask import Flask, render_template, request
import os
from modules.password_strength import analyze_password
from modules.hash_demo import generate_hash
from modules.simulation import brute_force_simulation
from modules.report_generator import generate_report

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/dictionary", methods=["GET", "POST"])
def dictionary():

    generated_words = []

    if request.method == "POST":

        name = request.form["name"]
        year = request.form["year"]

        generated_words = [
            name,
            name.capitalize(),
            name + year,
            name + "@123",
            name + "@2026",
            name + "123",
            name.capitalize() + "123",
            name + "!",
            name + "#",
            name + "$",
            name + "@",
            name + year + "!",
            name + year + "@",
            name.upper(),
            name.lower()
        ]

        os.makedirs("wordlists", exist_ok=True)

        with open("wordlists/generated.txt", "w") as f:

            for word in generated_words:
                f.write(word + "\n")

    return render_template(
        "dictionary.html",
        words=generated_words
    )


@app.route("/hash", methods=["GET", "POST"])
def hash_page():

    result = None

    if request.method == "POST":

        password = request.form["password"]
        algorithm = request.form["algorithm"]

        hash_value = generate_hash(password, algorithm)

        result = {
            "password": password,
            "algorithm": algorithm.upper(),
            "hash": hash_value
        }

    return render_template(
        "hash.html",
        result=result
    )


@app.route("/strength", methods=["GET", "POST"])
def strength():

    result = None

    if request.method == "POST":

        password = request.form["password"]

        score, strength, entropy, suggestions = analyze_password(password)

        result = {
            "score": score,
            "strength": strength,
            "entropy": entropy,
            "suggestions": suggestions
        }

    return render_template(
        "strength.html",
        result=result
    )


@app.route("/simulation", methods=["GET", "POST"])
def simulation():

    result = None

    if request.method == "POST":

        target = request.form["target"]
        charset = request.form["charset"]

        result = brute_force_simulation(
            target,
            charset
        )

    return render_template(
        "simulation.html",
        result=result
    )


@app.route("/report", methods=["GET", "POST"])
def report():

    message = None

    if request.method == "POST":

        generate_report()

        message = "Security audit report generated successfully!"

    return render_template(
        "report.html",
        message=message
    )


if __name__ == "__main__":
    app.run(debug=True)