import re
string = 'The asserts after your function you can use in order to check yourself by pressing the “Run” button.'
print(re.findall(r"\b\w{4,}\b", string))