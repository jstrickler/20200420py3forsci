#!/usr/bin/env python
import lxml.etree as ET

doc = ET.parse('DATA/solar.xml')

root = doc.getroot()

print(root.tag, '\n')

for element in root:
    if "planets" in element.tag:
        for planet in element.findall('planet'):
            print(planet.get('planetname'))
            for moon in planet.findall('moon'):
                print(f"    {moon.text}")


