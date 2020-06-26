import re
text = 'KBTU FIT, SDU FIT, KIMEP ISE'
pattern = 'FIT'
for match in re.findall(pattern, text):
    print('Exist "%s"' % match)