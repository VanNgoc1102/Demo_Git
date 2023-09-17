import re

str = 'urp-sl_ealice@google.com'
tuples = re.findall(r'([\w\.-]+)@([\w\.-]+)', str)
print(tuples[0][0])  
