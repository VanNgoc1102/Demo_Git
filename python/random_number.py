from random import randrange
somay=randrange(1,101)
solandoan=0
win=False
while solandoan<7:
    solandoan +=1   
    songuoi=int(input("Nhap so cua ban di [1..100]: " ))
    print("Ban doan lan thu :",solandoan)
    if somay==songuoi:
        print ("Ban doan trung roi. Chuc mung ban nhe!")
        win=True
        break
    elif somay<songuoi:
        print("Ban doan sai roi. So may < so ban!")
    else:
        print("Ban doan sai roi. So may > so ban")
if win==False :
    print("GAME OVER !")
    print("SO MAY LA",somay)
