import numpy.random as rd

def insert(st,x,k) :
    i = k - 1
    while (st[i] > x ) and (i >= 0) :
        st[i+1] = st[i]
        i = i -1
    st[i+1] = x
    
def main():
    st = rd.randint(100,size=(20))
    for i in range(1,len(st)) :
        insert(st,st[i],i)
    print(st)
    main()