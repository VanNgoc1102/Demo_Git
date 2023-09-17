
# def myfunc(n):
#   return lambda a : a * n

# mydoubler = myfunc(3)

# print(mydoubler(11))


def cube(y):
    return y*y*y

lamd_cube = lambda y:y*y*y

print("def function: ",cube(4))
print("lamda function: ", lamd_cube(4))