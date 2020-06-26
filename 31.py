import re
text = 'Shymkent 567, Aktau большой город'
print(re.sub("[ ,.]", ":", text))