#!/usr/bin/env python
import lxml.etree as ET

doc = ET.parse('DATA/solar.xml')

root = doc.getroot()

print(root.tag)

indent = '    '

for subroot in root:
    print(indent * 1, subroot.tag)
    for subroot2 in subroot:
        print(indent * 2, subroot2.tag)
        for sub3 in subroot2:
            print(indent * 3, sub3.tag)

