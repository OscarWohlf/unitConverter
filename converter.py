from flask import Flask, render_template, request

app = Flask(__name__)

# Conversion functions
def pounds_to_kg(pounds):
    return pounds * 0.453592

def kg_to_pounds(kg):
    return kg / 0.453592

def mph_to_min_sec_per_km(mph):
    km_per_hour = mph * 1.60934
    min_per_km = 60 / km_per_hour
    minutes = int(min_per_km)
    seconds = int((min_per_km - minutes) * 60)
    return f"{minutes} min {seconds} sec"

def min_per_km_mph(minPrKm):
    minutes = int(minPrKm)
    seconds = (minPrKm - minutes) / 0.60
    min_pr_km = minutes + seconds
    km_per_hour = 60 / min_pr_km
    mph = km_per_hour / 1.60934
    return round(mph, 1)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        conversion_type = request.form["conversion_type"]
        value = float(request.form["value"])
        
        if conversion_type == "pounds_to_kg":
            result = f"{value} pounds is {pounds_to_kg(value):.2f} kg"
        elif conversion_type == "kg_to_pounds":
            result = f"{value} kg is {kg_to_pounds(value):.2f} pounds"
        elif conversion_type == "mph_to_min_sec_per_km":
            result = f"{value} mph is {mph_to_min_sec_per_km(value)} per km"
        elif conversion_type == "min_per_km_mph":
            result = f"{value} min/km is {min_per_km_mph(value)} mph"
    
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
