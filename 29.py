import re

str = "So this mission is the easiest one. Write a function that will receive 2 numbers as input and it should"

for num in re.finditer("\d+", str):
    print(num.group(0))
    print("Index:", num.start())