list1 = [1,2,3,4,5,6,7,8,9,10]

def tables(a,b):
    z = 0
    for o in range (1,a+1):
        for i in range (1,b+1):
            z+= o
            print (o,"*",i,"=",z)
        z = 0
x = int(input ("How Many numbers?"))
tables (x,10)

y = 0
def add(a,b):
    y = a+b
    return y

c = add(2,4)
print (c)
print (add(1,2))
    
