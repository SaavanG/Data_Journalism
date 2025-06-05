import json

file = open("data/data_cleansed.csv", "r")
lines = file.readlines()

borough_acreage = {}

for i in range(1, len(lines)):
    line = lines[i]
    data = line.strip().split(',')
    
    acreage = float(data[0])
    borough = data[2]
    
    if borough not in borough_acreage:
        borough_acreage[borough] = 0
    borough_acreage[borough] += acreage

file.close()
