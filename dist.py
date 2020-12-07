from math import sin, cos, sqrt, atan2, radians

R = 6373.0

import csv

with open('out.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

for row in data:
    if row[0] == '110021.0':
        print(row)
        break



breakpoint()

lat1 = radians(52.2296756)
lon1 = radians(21.0122287)
lat2 = radians(52.406374)
lon2 = radians(16.9251681)

dlon = lon2 - lon1
dlat = lat2 - lat1

a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
c = 2 * atan2(sqrt(a), sqrt(1 - a))

distance = R * c

print("Result:", distance)
print("Should be:", 278.546, "km")
