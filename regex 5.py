import re

txt = "The rain in Spain falls stays mainly in the plain!"

x = re.findall("falls|stays", txt)

if x:
    print("Yes, there is at least one match")
else:
    print("No match")
