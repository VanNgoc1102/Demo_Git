#Required parameter & Default Parameter

#def print_name(name, greeting="Welcome "): #greeting =welcome la gia tri mac dinh
 #   print(f'{name},{greeting}')

# Variable- length parameters (*args and **kwargs)

def varibleLengthArgExample(a,b,*args, **kwargs):
    print(a,b)
    for arg in args:
    
        print(arg)
    for key , value in kwargs.items():
        print(key,value)


def main():
    #print_name("Nguyen Van Ngoc", "Xin chao mn")
    varibleLengthArgExample('a',2,"Hello world",1, size="Up size", age="NG")
    
if __name__=="__main__":
    main()