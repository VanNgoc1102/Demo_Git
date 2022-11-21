'''
viết chương trình khởi tạo List
-khởi tạo list
-thêm phần tử vào list
-nhập k, kiểm tra k xuất hiểu bao nhiêu lần trong list
-tính toongt các số nguyên tố trong líst
-sắp xếp
-xóa list'''
'''
from ast import If
from itertools import count
from pprint import pprint
from random import randrange

print("chương trình xử lí list:")
n=int(input("Nhập giá trị n:"))
lst=[0]*n
for i in range(n):
    lst[i]=randrange(-100,100)
print("List ngẫu nhiên la:")
print(lst)
print("Mời bạn nhập số mới:")
value=int(input())
lst.append(value)
print(lst)
k=int(input())
dem=lst.count(k)
print(k,"xuất hiên ",dem ," lần trong list!")

print(lst)
   
def CheckPrime(n):
    d=0
    for i in range(1,n+1):
        if n% i==0:
            d+=1
    return d==2

demnt=0
tongnt=0
for x in lst:
    
    if CheckPrime(x):
        demnt+=1
        tongnt+=x
print("Tổng các số Nguyên Tố trong list la: ",tongnt)
lst.sort()
print("List sau khi sort :")
print(lst)

'''
''''
from random import randrange


ls=[]
print("nhập số phần tử :")

n=int(input())

for i in range(n):
    ls.append(randrange(0,100))
print (" List sau khi tạo ngẫu nhiên là: ")
print(ls)
print("nhập số  k :")
k=int(input())
while ls.count(k)>0:
    ls.remove(k)

print("List sau khi xóa là : ",ls)
def checkDX(ls):
    for i in range(len(ls)):
        if ls[i]!= ls[len(ls)-i-1]:
            return False
    return True
kt=checkDX(ls)
if kt==True:
    print ("List đối xứng !")
else:
    print ("List ko đối xứng !")
'''
# bài tập rèn luyện list đa chiều
from random import randrange
from re import I


def TaoMaTran(m,n):
    D=[]
    for i in range(m):
        row=[]
        for j in range(n):
            row.append(randrange(0,100))

        D.append(row)

    return D
def xuatMaTran(D):
    for row in D:
        for element in row:
            print(element,end='\t')
        print()
def  LayDong(r):
    R=D[r]
    return R
def XuatList1chieu(R):
      for i in R:
          print(i,end='\t')
def  Laycot(c):
    C=[]
    for i in range(len(D)):
        C.append(D[i][c])
    return C
    
m =int(input("Enter Row :"))
n=int(input("Enter column: "))
D=TaoMaTran(m,n)
xuatMaTran(D)
k=int(input("Nhap so dong can xuat :"))
XuatList1chieu(LayDong(k))
c=int(input("\nNhap so cot can xuat :"))
XuatList1chieu(Laycot(c))
#xuat so max trong ma tran
def MAX (D):
    max=D[0][0]
    for i in range(len(D)):
        for j in range(len(D[i])):
            if D[i][j]>max:
                max=D[i][j]
    return max
print ("\nGia tri lon nhat cua D la:", MAX(D))


