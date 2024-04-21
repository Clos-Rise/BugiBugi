from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("main.html")

@app.route("/sas")
def sas():
    return render_template("sas.html")

@app.route("/secret")
def secret():
    return render_template("secret.html")

if __name__ == "__main__":
    app.run(debug=True)
