
def cToFconverter():
    while True:
        cTemp=input("Please enter C degree: ")
        if cTemp:
            cTemp=float(cTemp)
            fTemp=round(9*cTemp/5+32,1)
            print(f"{cTemp} C is converted to {fTemp}F")
            break
        else:
            print("cTemp input is empty")
            continue
def main():
    
    
    #print("Hello World")
    cToFconverter()
if __name__=="__main__":
    main()
