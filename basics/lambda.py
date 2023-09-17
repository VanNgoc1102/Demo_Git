#Ham an danh -lambda of python
#code=lambda so: so + 69
#def code1(so):
   # return so+69
#print(code(1))

code=lambda x,y,z :x+y-z
print(code(6,7,9))

'''
custom sorting using a lambda function as key parameter
'''
'''
coordinate2D=[(6,9), (9,6),(-1,3),(2,10)]
print(sorted(coordinate2D))
print(sorted(coordinate2D, key=lambda point: point[1]))
'''
'''
number_list =[5,3,-2,4,1,-1,-3,4,5]
print(sorted(number_list))
print(sorted(number_list, key=lambda x:abs(x)))
'''
'''
#map(func,seq), transforms each element with the function.
list_keyword=["codex","welcome","you"]
print(list(map(lambda x:x.title(), list_keyword)))
#['Codex', 'Welcome', 'You']


#cach 2
new_list=[keyword.title() for keyword in list_keyword ] 
print(new_list)
#['Codex', 'Welcome', 'You']
'''
#filter(func, seq), returns all elements for which func evaluates to True
list_number =[1,2,3,4,5,6,7,8,9,10]
print(list(filter(lambda x: x% 2!=0, list_number)))
#[1, 3, 5, 7, 9]

#cach 2
new_list=[x for x in list_number if x%2!=0]
print(new_list)
#[1, 3, 5, 7, 9]
 