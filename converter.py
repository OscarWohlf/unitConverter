from flask import Flask, render_template, request

app = Flask(__name__)

def mph_min_per_km(mph):
    km_per_hour = mph * 1.60934
    min_per_km = 60 / km_per_hour
    minutes = int(min_per_km) 
    seconds = int((min_per_km - minutes) * 60) 
    return minutes + (seconds/100)

def min_per_km_mph(minPrKm):
    minutes = int(minPrKm)
    seconds = (minPrKm - minutes) / 0.60
    min_pr_km = minutes + seconds
    km_per_hour = 60 / min_pr_km
    mph = km_per_hour / 1.60934
    return round(mph,1)

def pounds_to_kg(pounds):
    kg = pounds * 0.453592
    return kg

def kg_to_pounds(kg):
    pounds = kg / 0.453592
    return pounds

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        conversion_type = request.form["conversion_type"]
        value = float(request.form["value"])

        if conversion_type == "mph_min_pr_k":
            result = mph_min_per_km(value)
        elif conversion_type == "min_pr_k_mph":
            result = min_per_km_mph(value)
        elif conversion_type == "pounds_to_kg":
            result = pounds_to_kg(value)
        elif conversion_type == "kg_to_pounds":
            result = kg_to_pounds(value)

    return render_template("index.html",result= result)

if __name__ == "__main__":
    app.run(debug=True)