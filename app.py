from flask import Flask, render_template
import data

tours = data.tours  # список туров
departures = data.departures  # направления
app = Flask(__name__)


@app.route('/')
def main():
    b={}
    for i in tours:
        if i<=6:
            defy = tours[i]
            b[i] = defy
    return render_template('index.html', tours=tours, departures=departures, b=b)  # Главная


@app.route('/departures/<departure>/')
def departure(departure):
    b = {}
    for i in tours:
        if departure in tours[i].values():
            defy = tours[i]
            b[i] = defy
    return render_template('departure.html', b=b, tours=tours, departures=departures, departure=departure)  #
    # Направления


@app.route('/tours/<int:id>/')
def tour(id):
    b = {} # один тур
    for i in tours:
        if id == i:
            defy = tours[i]
            b[i] = defy
    return render_template("tour.html", b=b, tours=tours, departures=departures, id=id)  # Тур конкретный


app.run()
