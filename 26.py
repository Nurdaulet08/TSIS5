import re

lists = ["Peter Pan", "KBTU FIT", "Start Run"]

for list in lists:
        find = re.match("(P\w+)\W(P\w+)", list)

        if find:
            print(find.groups())