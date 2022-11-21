from numpy import sort
import numpy.random as rd

st = rd.randint(100,size=(20))

x = st[1]
st = sort(st)
print(st)
def binary_search_algorithm(st, x) :
    l = 0
    r =len(st)-1
    while (l <= r) :
        c =(l + r) // 2
        if (st[c] == x) :
            return(x,'address', c)
        elif (st[c] > x ) :
            r = c - 1
        else:
            l = c + 1

def main():
    find=binary_search_algorithm(st, x)
    print(find)

if __name__ =="__main__":
    main()