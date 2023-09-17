#Basics_Data_Type:
'''
Cac kieu du lieu trong Python:
bool; None, int,float, str

'''
'''
topic 1: bool & None'''
# bool :True & False

'''
var_bool= True
print(type(var_bool))
#None : phan tu rong
var_none=None
print(type(var_none))
# Numbers : int(so nguyen) &  float (so thuc)
print(10//3) # chia 3 lay phan nguyen => kq=3
round(6.79) # 7
round(6.667,2) # lam tron phan thap phan thu 2 =-> 6.67
'''

'''topic 2: string
#mutable: thay đổi được
list
dict
set
bytearray
# immutable: ko thay đổi được
int
float
decimal
complex
bool
bytes
string
tuple
range
frozenset

'''
'''
#escaping Backslash \
my_string='"i\'m a student"'
print(my_string,type(my_string))
sub_string=my_string[::-1] # reverse the string :đảo ngc xâu
#join elements of a list into a string :   .join()
my_list=['how', 'are','you','doing']
sentence='*'.join(my_list) #nối chuỗi lại với nhau
print(sentence)

#hàm strip()   xóa tất cả khoảng trống
s="   i am alone"
print(s.strip())
print(s.strip('e'))
#hàm split()
print('but life is good'.split()) 
#tách chuỗi thành khoảng tùng đoạn khoảng trắng


#hàm replace()
#thay thế 1 số từ trong chuỗi
print('Help me'.replace("me","you"))
'''

'''
String formatting
#   %,.format() , f-Strings
'''
'''
name="CodeXplore"
my_string="welcome to %s"% name #%s là kiểu xâu
pi=3.15159
ss="pi number"
my_string="variable is %.2f from %s"%(pi,ss) # %.2f :2 chữ số thập phân

print(my_string)


#.format()
age =20
height =170.5
my_string= "i am {} years old; {:.3f} cm".format(age, height)
print(my_string)


# f-String
pi=3.14159
name="Nguyen Van Ngoc"
my_string=f"Pi is {pi:.2f} and my name is {name}"
print(my_string)

'''
#1 creating a list
'''
list_1=["banana", "apple","orange","cherry"]
list_2=[5,"code ",False,None]
list_3=list()
print(list_3)
'''
#2. access elements: truy cap cac gia tri trong list
'''
my_list=[1,2,'3', True]
print(len(my_list))
print(my_list.index('3'))
for item in my_list:
    print(item)
#python's built -in emumerate function
presidents=["washington","adams","jackson","obama","trumd"]
print(presidents)
for index, president in enumerate(presidents, start=1):
    print(f"President #{index} :{president}")

#slicing
#: is called slicing and had the format [start :end: step] : cut
my_list=[1,2,'3', True]
print(my_list[1:])
print(my_list[:1])
print(my_list[::-1]) # đao ngc xâu
#3.1 add  to list
print(my_list*2) # lap lai 2 lan

print(my_list+[100,'vanngoc'])
print(my_list)
#ham my_list.append(100) # add ddc 1 gt
#my_list.extend([100, "vanngoc"]) # add dc 1 list
print(my_list.extend([100,"vanngoc"])) 
#my_list.extend([100, "vanngoc"]) # add dc 1 list
print(my_list)
# 3.2.sroting
my_list=[1,4,2,3,6,3]
my_list.sort()# tang dan
#  my_list.sort(reverse=True) # sap xep giam dan

print(my_list)
'''


'''
4. List  comprehensions

list comprehensions  giúp bạn viết code ngắn gọn ( đặc biệt khi đang ở
trong một vòng lặp đã có ) và dễ đọc và nhìn code dễ hơn
'''
'''
word="Hello world"
print([char for char in word]) 
#out:  ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
even_number=[ i for i in range(0,10) if  i % 2==0]
print(even_number)
# out:   [0, 2, 4, 6, 8]

transactions=[100,200,300,150,80]
tax_rate=0.08
service_charge=0.07
def get_price_service(bill):
    return bill*(1+tax_rate+service_charge)
final_prices=[get_price_service(bill) for bill in transactions]
print(final_prices)
#
# [115.00000000000001, 230.00000000000003, 345.00000000000006, 172.50000000000003, 92.00000000000001]
'''

# Advanced Functions
#list() > convert string 
'''
from array import array


my_strings="Welcome to Hanoi"
list_of_chars=list(my_strings)
print(list_of_chars) 
#out:  ['W', 'e', 'l', 'c', 'o', 'm', 'e', ' ', 't', 'o', ' ', 'H', 'a', 'n', 'o', 'i']
# sum()
print(sum([1,2,5,6,7]))
#zip(): looping through two list simultanrously(dong thoi)
wizards=["harry potter", "ron","hermione"]
pets=["dog","cat","brid"]
for wiz, pet in zip(wizards, pets):
    print(f'{wiz} has {pet}')
#harry potter has dog
#ron has cat
#hermione has brid
'''
#5. 2D array/list =Matrix: mang 2 chieu
'''
matrix= [[1,2,3],
         [4,5,6],
        [7,8,9]]
for row in range(len(matrix)):
    for col in range(len(matrix)):
        print(matrix[row][col])
print(matrix[1][2])

#transform Matrix in list
list_converter=[matrix[row][col] 
                for row in range(len(matrix)) for col in range(len(matrix))]
print(list_converter)
#[1, 2, 3, 4, 5, 6, 7, 8, 9]
# combine columns with zip and *
print([x for x in zip(*matrix)])
'''

#loop
my_list=[1,2,3]
my_dict={'a':1,'b':2,'c':3}
for  key ,value in my_dict.items():
    print(key,value)
msg=''
while msg !='quit':
    msg=input("please give me an input: ")
    print(msg)