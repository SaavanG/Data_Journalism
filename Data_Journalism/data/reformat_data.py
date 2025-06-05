import json

file = open("Data_Journalism/data/data_cleansed.csv", 'r') 
lines = file.readlines()

borough_zip_acreage = {}

for i in range(1, len(lines)):
   line = lines[i]
   data = line.strip().split(',')

   acreage = float(data[0])
   borough = data[2]
   zipcode = data[3].strip(',')

   zipcode = zipcode.replace('"', '').strip()

   if ',' in zipcode:
       zipcodes = [z.strip() for z in zipcode.split(',')]
   else:
       zipcodes = [zipcode]
   if borough not in borough_zip_acreage:
       borough_zip_acreage[borough] = {}

   for zipcode in zipcodes:
       if zipcode not in borough_zip_acreage[borough]:
          borough_zip_acreage[borough][zipcode] = 0
       borough_zip_acreage[borough][zipcode] += acreage

file.close()

with open("Data_Journalism/data/data.json", 'w') as json_file:
    json.dump(borough_zip_acreage, json_file, indent= 3)