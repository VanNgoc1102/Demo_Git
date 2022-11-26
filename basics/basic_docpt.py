# BASIC

# cac ham toan hoc
'''
from math import * #dung thu vien de khai bao cac ham toan hoc
x=5
y=7
print(pow(x,y))
print(x**y)
print(sqrt(25))
do=30
print("30=>", radians(do))
rad=radians(do)
rad=radians(do)
print(degrees(rad)) #ham chuyen radian ve do
print("log10(1000)= ",log10(1000))
#luong giac
print ("moi ban nhap 1 goc")
goc=float(input())
sinx=sin(radians(goc)) # chuyeenr ve radian nhes
cosx=cos(radians(goc))
tanx=tan(radians(goc))
cotx=1/tanx
print("sin({0})={1}".format(goc,sinx))# la format
print("cos({0})={1}".format(goc,cosx))
print("tan({0})={1}".format(goc,tanx))
print("cot({0})={1}".format(goc,cotx))
'''
# ham romdom
'''
from random import randrange


while True:
    x=randrange(-100,100)
    print(x,end=',')
    if x==50:
        break
print("BYE !")
'''
#HAM EXIT
'''
from cgi import print_form


while True:
    print ("Nhat 1 so: ")
    n=int(input())
    count=0
    for i in range(1,n+1):
        if n% i==0 :
            count+=1
    if (count==2):
        print(n,"la so nguyen to")
    else:
        print(n,"Ko la so nguyen to")
    print("Tiep tuc ko ? (c/k): ")
    if input()=="k":
        exit()
    print("BYE !")#exit laf no tat han luon

'''#Ham eval => rat manh
'''
from math import *
from unicodedata import name
s="(5*6)-(7/2)+8+sin(0.5)"
x=eval(s)
print(x)

x1,x2=eval(input("Nhap x1,x2 :"))
print("x1=",x1,"x2=",x2)

#ucln
'''
'''
def UCLN(a,b):
    #hàm dùng ucln vda=9,b=6 ucln=3
    while (a - b !=0):
        if a>b:
            a=a -b
        else :
            b=b -a
    return a
print(UCLN(10,6))
'''

# parameder mac dinh

'''def Fn(n,m=0):
    s=0;
    for i in range(1,m+n,1):
        s+=i
    return s
print (Fn(5))
print (Fn(5,1))

def Fn2(n,m=1,k=2):
    s=0
    for i in range(1,m+n+k,1):
        s+=i;
    return s
print("*"*30)
print (Fn2(5))
print(Fn2(5,3)) #1+2+3+3+4+5+6+7+8+9 chu y m=3,n=5
print(Fn2(5,k=4)) #n=5,m=1,k=5

print("*"*30)
lst=["obama","putin","kimjong un"]
for item in lst:
    print(item,end='\t')'''

#landa exention
'''
def handle(f,x):
    return f(x)
kq1=handle(lambda x:x**2,9) #truyen 9 vao x**2
print(kq1)
kq2=handle(lambda x:x%2==0,4) #ghi tuong minh
print("kq2=",kq2)

def lasochan(x):
    return x%2==0
kq3=handle(lasochan,4) #ghi ngan gon hoi kho hieu
#handle(lasochan,4)=handle(lambda x:lasochan(x),4)
print("kq3=",kq3)
kq4=handle(lasochan,5)
print("kq4=",kq4)
'''

#DE QUY
'''
def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)
print(factorial(6))

'''
#bai tap BIM
'''
def BMI(height,weight):
    return weight/(height**2)
def phanloai(bmi):
    if bmi<18.5 :
        return "Gay"
    elif bmi<=24.9 :
        return "binh thuong"
    elif bmi<=29.9 :
        return "hoi beo"

    elif bmi<=34.9 :
        return "beo cap 1"
    elif bmi<=39.9 :
        return "beo cap do 2"
    else:
        return "beo phi cap 3"
def Nguycobenh(bmi):
    if bmi<18.5 :
        return "Thap"
    elif bmi<=24.9 :
        return "Trung binh"
    elif bmi<=29.9 :
        return "cao"

    elif bmi<=34.9 :
        return "cao"
    elif bmi<=39.9 :
        return "Rat cao"
    else:
        return "Nguy hiem"
print("Nhap vao chieu cao: ")
height=float (input())
print("Nhap vao can nang: ")
weight=float (input())
bmi=BMI(height,weight)
print("BMI cua ban la: ",bmi)
print("Phan loai cua ban la:",phanloai(bmi))
print("Nguy co benh cua ban: ",Nguycobenh(bmi))

'''
#bai tap ROI (return on Investment)
'''
def  ROI(dt,cp):
    return (dt-cp)/cp
def GoiYDauTu(roi):
    if roi>0.75:
        return "Nen DauTu"
    else:
        return "Ko DauTu"
print ("Chuong Trinh Tinh ROI")
dt=int(input("Nhap Doanh Thu: "))
cp=int (input("Nhap chi phi :"))
roi=ROI(dt,cp)
print("Ti le Roi=",roi)
print("==>",GoiYDauTu(roi))
'''
#CHUOI
''''
from unittest.mock import NonCallableMagicMock


print ("Moi ba nhap ten :")
name=input()
print("Ten ban nhap: ", name)
print(name.upper())
print(name.lower())
'''
#rjust: can phai, ljust : lawn trai, center: can giua
'''
s="docs.google.com/"
print (s)
print (len(s))# ~print(s.__len__())
s1="0359074987"
s2="https://www.youtube.com/"

print (s.rjust(24,"*")) #can phai
print (s1.rjust(24,"*"))
print (s2.rjust(24,"*"))
'''
#ham strip() xóa khoang trang
'''
s1="   Hello Obama   "
print(s1,len(s1))
s2=s1.strip() # xóa khoang trang
print(s2,len(s2))
print("*"*30)
s3="##Trum##"
s3=s3.strip("#")
print(s3)
'''

#ham kiểm tra có chứa chuỗi con nào ko
#endswith  startswith
'''
s="C:/music/bolero/seve.mp4"
if s.endswith(".mp3"):
    print("Bai hat nay có định dạng MP3")
else:
    print("Bai hat nay không định dạng MP3")
s2="*** obama##"
print(s2.startswith("$"))

def locSDT(dauso):
    dsArr=["0359074987","0359034733","0328483421","0329938383"]
    for phone in dsArr:
        if (phone.startswith(dauso)):
            return phone
    return "<empty>"
print("Mời bạn nhập đầu số : ")
dauso=input()
phone=locSDT(dauso)
print(phone)
def loc_Toan_bo_sdt(dauso):
    dsArr=["0359074987","0359034733","0328483421","0329938383"]
    dsFound=[]
    for phone in dsArr:
         if (phone.startswith(dauso)):
             dsFound.append(phone)
    return dsFound
dauso=input("Nhap dau so: ")
dsFound=loc_Toan_bo_sdt(dauso)
print(dsFound)
'''
#ham find, rfind ,count : tìm thấy dầu tien,vị trí cuối, và đếm  count
'''
s="C:/music/bolero/save me .mp3"
p1=s.find('/')
p2=s.rfind('/')
print("p1 =",p1)
print("p2 =",p2)

c=s.count("o")
print("o xuất hiện =",c)
'''
'''
z = 3 + 2j
print(type(z))
'''
#hàm format và substring
'''
s="d:/tailieu/python/code.pdf"
p=s.rfind('/') #vị trí cuối của /
print(s[p+1:])
p2=s.rfind('.')
print(s[p+1 :p2])
'''
#ham split: tách chuôi mảng con 
'''
s="sv007; Nguyen thi nu;1/1/2002"
arr=s.split(';') #split (';') xóa ; và chia thành xau con
print(len(arr))
for x in arr:
    print(x)

s="""obama
    hahaha
    alibaba"""
ar=s.splitlines()   # Hoi khac với split 1 tí
for line in ar:
    print(line,"a->",line.count("a"))
s="""sv01;Nguyen thi thanh; 1/1/1990
sv02;Nguyen thi hanh; 1/1/1956
sv03;Nguyen thi anh; 1/1/1910
sv04;Nguyen thi an; 1/1/1910
"""
arSV =s.splitlines()
for line in arSV:# strip () xóa khoảng trăng
    arrInfor=line.strip().split(';')
    if len(arrInfor)==3:
        print(arrInfor)
'''
'''
#hàm join :hàm nói chuỗi
s="sv02;Nguyen thi hanh;1/1/1956"
arr=s.split(';')
print(len(arr))
for x in arr:
    print(x)
s2="."
s2=s2.join(arr) #nối chuỗi bằng dấu chấm (.)
print(s2)

a="obamma"
b="kimjongun"
c=a+b
print(c)
'''

#BÀI TẬP CHUỖI ĐÔI XỨNG
def checkDoiXung(s):
    check=True
    for i in range(len(s)):
        if (s[i] != s[len(s)-1-i]):
            check=False
            break
    return check
def main():
    s=input("nhap chuoi bat kì : ")
    if (checkDoiXung(s)):
        print('là chuoi đối xứng')
    else:
        print('ko là chuoi đối xứng')
main()


'''
#Bai tâp tối ưu chuôi
def ToiUuChuoi(s):
    s2=s
    s2=s2.strip()
    arr=s2.split(' ')
    s2=""
    for x in arr:
        word=x
        if len(word.strip()) != 0:
            s2=s2+word+" "
    return s2.strip()
s="    Nguyen     Van     Ngoc       "
print(ToiUuChuoi(s))
'''
# LIST TRONG PYTHON
'''

from random import randrange
print("Moi bạn nhap số phần tử: ")
n=int(input())
lst=[0]*n 
for i in range(n):
    lst[i]=randrange(-100,100)
print(lst)
print("Duyệt theo collection:")
for x in lst :
    print(x, end='\t')
print("\n Duyệt theo Index:")
for x in range(len(lst)) :
    print(lst[x], end='\t')
print("\n Duyệt theo ngược từ cuối lên:")
for x in range(len(lst)-1,-1,-1) :
    print(lst[x], end='\t')
'''
#lst.insert(vitrichen, giá trị chen)
#lst.append (gtri) chỉ chèn ở cuối danh sach
#lst.remove(gtri): xóa giá trị dầu tiên của sanh sách
# ngoài ra còn có sử dụng del
'''
lst=[1,2,3]
print(lst)
lst.insert(0,999)
print(lst)
lst.append(338)
print(lst) # có thể chèn vào 1 mảng con
lst.append([332, 444])
print(lst)
lst.remove(1) #xóa giá tri 1
print(lst)
lst =[113,45,34,2,555,552,235]
# ngoài ra còn có sử dụng del
del lst[0] #xoa phần tử ở vitri thứ 0
print(lst)
del lst[1:4] # xóa các phần tử thứ 1 đến thứ 3
print(lst)
# hàm reverse : đảo ngc danh sách ban đầu thay đổi gt
lst =[113,5,34,2,555,522,235]
#lst.reverse() 
print(lst) #[235, 522, 555, 2, 34, 5, 113]
for i in range(len(lst)-1,-1,-1):
    print(lst[i],end='\t') #đảo ngc nhưng ko thay dổi gt đầu
'''
# SLICING DÙNG ĐỂ TRICH LỌC
#list[begin:end:step]
'''
lst =[1,45,34,2,5,552,235]
print (lst[0:3])
print (lst[0:5:2])
'''

# List
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
'''
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


'''

# list đa chiều
'''
from random import randrange


lst =[[4,5,6],
    [7,10,5],
    [-7,9,2] 
    ]
print(lst)
#c1:
for row in lst:
    for column in row:
        print(column,end='\t')
    print ()
print("*"* 20)
#c2
for i in range(len(lst)):
    for j in range(len(lst[i])):
        print(lst[i][j],end='\t')
    print()

#khởi tạo matran 2 chiều bất kì
arr2D=[]
rowsize =int(input("Nhap so dong: "))
columnsize =int(input("Nhap so cot: "))
for i in range(rowsize):
    onerow =[]
    for j in range(columnsize):
        onerow.append(randrange(-100,100))
    arr2D.append(onerow)
print ("Ma trân bất kì là: ")
for i in range(len(arr2D)):
    for j in range(len(arr2D[i])):
        print(arr2D[i][j],end='\t')
    print()
'''