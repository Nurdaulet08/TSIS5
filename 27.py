import re

str = "Pavlodar 777, Shymkent 667, Aktau 45"
result = re.split("\D+", str)

for element in result:
    print(element)