import re

p = re.compile(r'[.?!]+')

string = 'Elizabeth likes water. She also likes soda.  Does she like soda? I am not sure!'

print(p.split(string))