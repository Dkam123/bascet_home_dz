from flask import Flask, render_template

app = Flask(__name__)
app.debug = True



user = {
    "name": "Michael Jordan",
    "name2": "Shaquille O'Neal",
    "name3": "LeBron James",
}

@app.route("/")
def hello():
    return render_template("player.html", user=user)


@app.route("/profile")
def profile():
    return render_template("profile.html", user=user)


@app.route("/card")
def card():
    return render_template("card.html", user=user)


@app.route("/card1")
def card1():
    return render_template("card1.html", user=user)


@app.route("/card3")
def card3():
    return render_template("card3.html", user=user)



app.run()