import re

s = '''Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code 
        readability with the use of significant indentation. Python is dynamically-typed and garbage-collected.
        It supports multiple programming paradigms, including structured, object-oriented and functional programmin
        Designed by: Guido van Rossum
        First appeared: 20 February 1991; 31 years ago 10/26/2022 17:23:52'''

d = re.findall(r'\d{1,5}', s) # select all numbers are  1-5 char long
st = re.findall(r'[a-z]{10,15}', s) # select all string are  10-15 char long
low = re.findall(r'[A-Z]\w{1,}\s', s) # select all lower string star 1 char long

print(d)
print(st)
print(low)

list  = '132 Cầu Giấy, Quán Hoa, Hà Nội	'