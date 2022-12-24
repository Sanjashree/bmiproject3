from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/bmi", methods=["POST", "GET"])
def bmi():
    if request.method == "POST":
        age = float(request.form["age"])
        height = float(request.form["height"])
        weight = float(request.form["weight"])
        return render_template("bmi.html", age=age, height=height, weight=weight)
    else:
        return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True, port=5001)
