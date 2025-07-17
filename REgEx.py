import re

txt = "The rain in Spain me a"
pattern = "ra.+e"
x = re.findall(pattern, txt)
if x:
    print("yes, This one ready")
else:
    print("No, this one")