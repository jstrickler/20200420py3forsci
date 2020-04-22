#!/usr/bin/env python
import lxml.etree as ET

doc = ET.parse('DATA/solar.xml')

# doc.findall() same as doc.getroot().findall()
for planet in doc.findall('.//planet'):
    name = planet.get('planetname')
    print(name)
    for moon in planet.findall('moon'):
        print(f"    {moon.text}")
