from flask import Flask, render_template, session, request, jsonify, redirect, url_for
from os import environ

app = Flask(__name__, static_folder='static/', static_url_path='')
app.secret_key = "uashdohasidhuawhdquiehdoijcxzovnjzxo"

users = [
    ["admin", "password"],
    ["hej", "test"]
]

@app.route("/")
def index():
    if not "loggedin" in session:
        return redirect(url_for("login"))

    return render_template("index.html", user=session["loggedin"])

@app.route("/login")
def login():
    return render_template("login.html")

@app.post("/logincheck")
def logincheck():
    query = request.json.get("details")

    print(query)
    if not query in users:
        return jsonify({"status": False, "message": "An error occured"})
    
    session["loggedin"] = query
    return jsonify({"status": True})

if __name__ == '__main__':
    app.run("0.0.0.0", 5000, True)