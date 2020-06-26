import re

IP = str(input())
string = re.sub('\.[0]*', '.', IP)
print(string)


#ip = "3506.8630.090.759"