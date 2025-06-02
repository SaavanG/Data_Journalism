from flask import Flask, render_template, request, send_from_directory
import json
from static import images


app = Flask(__name__, static_url_path='', static_folder='static')


@app.route('/')
def home():
    return render_template('about.html')

@app.route('/city')
def citypage():
    with open("data/parks_by_borough.json") as f:
        data = json.load(f)

    borough_totals = {}
    for borough_code, zip_dict in data.items():
        total = sum(zip_dict.values())
        borough_totals[borough_code] = round(total, 2)

    def scale_to_lightness(value, min_val, max_val):
        lightness = 85 - ((value - min_val) / (max_val - min_val)) * 50
        return round(max(35, min(85, lightness)))

    min_total = min(borough_totals.values())
    max_total = max(borough_totals.values())

    borough_lightness = {
        k: scale_to_lightness(v, min_total, max_total)
        for k, v in borough_totals.items()
    }

    return render_template(
        "city.html",
        B=borough_lightness.get("B", 50),  #Brooklyn
        M=borough_lightness.get("M", 50),  #Manhattan
        Q=borough_lightness.get("Q", 50),  #Queens
        R=borough_lightness.get("R", 50),  #Staten Island
        X=borough_lightness.get("X", 50)   #Bronx
    )


@app.route('/manhattan')
def manhattanpage():
    with open("data/parks_by_borough.json") as f:
        data = json.load(f)
    return render_template("manhattan.html", zip_acreage=data["M"])

@app.route('/bronx')
def bronxpage():
    with open("data/parks_by_borough.json") as f:
        data = json.load(f)
    return render_template("bronx.html", zip_acreage=data["X"])

@app.route('/queens')
def queenspage():
    with open("data/parks_by_borough.json") as f:
          data = json.load(f)
    return render_template("queens.html", zip_acreage=data["Q"])

@app.route('/statenisland')
def statenislandpage():
    with open("data/parks_by_borough.json") as f:
        data = json.load(f)
    return render_template("staten_island.html", zip_acreage=data["R"])

@app.route('/brooklyn')
def brooklynpage():
    with open("data/parks_by_borough.json") as f:
        data = json.load(f)
    return render_template("brooklyn.html", zip_acreage=data["B"])



if __name__ == '__main__':
    app.run(debug=True, port=5001)
