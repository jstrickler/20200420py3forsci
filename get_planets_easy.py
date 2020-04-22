#!/usr/bin/env python
import lxml.etree as ET
import csv

doc = ET.parse('DATA/solar.xml')

# doc.findall() same as doc.getroot().findall()
with open('planets.csv', 'w') as planets_out:
    wtr = csv.writer(planets_out)
    for planet in doc.findall('.//planet'):
        name = planet.get('planetname')
        print(name)
        fields = [name]
        for moon in planet.findall('moon'):
            moon_name = moon.text
            fields.append(moon_name)
            print(f"    {moon_name}")
        wtr.writerow(fields)
