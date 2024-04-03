import xml.etree.ElementTree as ET

tree = ET.parse('3 - 2.osm')
root = tree.getroot()


number_24h = 0
for tag in root.findall("./node/tag/[@v='24/7']"):
    number_24h += 1

print("Работающих круглосуточно:", number_24h)

list_hours = []
number_11to23 = 0
number_10to22 = 0

for tag in root.findall("./node/tag/[@k='opening_hours']"):
    name = tag.get('v')
    list_hours.append(name)

for i in list_hours:
    if '11:00-23:00' in i:
        number_11to23 = number_11to23 + 1
    if '10:00-22:00' in i:
        number_10to22 = number_10to22 + 1
print("Работающих c 11 до 23:", number_11to23)
print("Работающих с 10 до 22:", number_10to22)
