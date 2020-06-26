import re
str = 'KBTU TOP, ENU BOT.'
print(re.sub("[ ,.]", ":", str, 2))