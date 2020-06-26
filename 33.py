import re
str = 'This is Pavlodar 777'
print(re.findall(r"\b\w{3}\b", str))