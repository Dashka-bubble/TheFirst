from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')  # Главная


@app.route('/departures/<departure>/')
def departure(departure):
    return render_template('departure.html')  # Направления


@app.route('/tours/<id>/')
def tour(id):
    return render_template("tour.html", )  # Туры



app.run()