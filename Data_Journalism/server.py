from flask import Flask, render_template, request, send_from_directory
import json

app = Flask(__name__, static_url_path='', static_folder='static')


@app.route('/')
def home():
    return render_template('about.html')

@app.route('/city')
def citypage():
    with open("Data_Journalism/data/data.json") as f:
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

@app.route('/borough/<name>')
def borough_page(name): 
    with open("Data_Journalism/data/data.json") as f:
        data = json.load(f)
        borough_names = {
        "manhattan": "M",
        "brooklyn": "B",
        "queens": "Q",
        "bronx": "X",
        "staten-island": "R"
    }
    if name not in borough_names:
        return "borough not found", 404
    borough_code = borough_names[name]
    zip_acreage = data.get(borough_code, {})
    total = sum(zip_acreage.values())

    return render_template("borough.html", 
                           zip_acreage = zip_acreage,
                           borough_name=name.replace("-", " ").title(),
                           total_acreage = round(total,1)
                            )
if __name__ == '__main__':
    app.run(debug=True, port=5001)
