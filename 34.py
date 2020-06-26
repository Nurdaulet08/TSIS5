import re
str = 'The asserts after your function you can use in order to check yourself by pressing the “Run” button'
print(re.findall(r"\b\w{3,5}\b", str))