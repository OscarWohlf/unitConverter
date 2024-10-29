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

print(mph_min_per_km(8.7))
print(min_per_km_mph(4.17))
print(pounds_to_kg(225))