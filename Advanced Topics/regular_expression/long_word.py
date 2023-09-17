import re

s = '''Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code 
        readability with the use of significant indentation. Python is dynamically-typed and garbage-collected.
        It supports multiple programming paradigms, including structured, object-oriented and functional programmin
        Designed by: Guido van Rossum
        First appeared: 20 February 1991; 31 years ago '''

i = 1
while True:
    kq = re.findall(r'\w{'+str(i)+',}',s)
    if len(kq) == 0:
        break
    i+=1
i-=1
kq= re.findall(r'\w{'+str(i)+',}',s)
print(kq)