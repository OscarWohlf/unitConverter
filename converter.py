def mph_to_min_sec_per_km(mph):
    km_per_hour = mph * 1.60934
    min_per_km = 60 / km_per_hour

    minutes = int(min_per_km) 
    seconds = int((min_per_km - minutes) * 60) 
    
    return minutes, seconds

print(mph_to_min_sec_per_km(8.7))