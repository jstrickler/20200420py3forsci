#!/usr/bin/env python
import lxml.etree as ET

superheroes = [
    ('Superman', 'Clark Kent', 'Metropolis', "DC"),
    ('Batman', 'Bruce Wayne', 'Gotham City', "DC"),
    ('Ant-man', 'Hank Pym', 'Chicago', "Marvel"),
    ('Wonder Woman', 'Diana Prince', 'Los Angeles', "DC"),
]

root = ET.Element('superheroes')
for name, secret_identity, city, universe in superheroes:
    sh = ET.SubElement(root, 'superhero', universe=universe)
    ET.SubElement(sh, 'name').text = name
    si = ET.SubElement(sh, 'secret_identity')
    si.text = secret_identity
    ET.SubElement(sh, 'city').text = city

doc = ET.ElementTree(root)
doc.write("superheroes.xml", pretty_print=True, xml_declaration=True)




raw_xml = ET.tostring(root, pretty_print=True, xml_declaration=True)
xml = raw_xml.decode()  # convert bytes to str

print(xml)

