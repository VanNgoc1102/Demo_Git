import numpy.random as rd

st = rd.randint(100,size=(20))
st = list(st)
print(st)
m = st.pop()

while (st != []) :
    b = st.pop()
    if (b > m) :
        m = b
print("Max = ",m) 