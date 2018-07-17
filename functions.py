def f1():
        print ("ahh")
        print ("ah2")
f1()
def f2(x):
        return 2*3*x
print (f2(3))
def f3 (x, y):
        return 2*x*(y**2)
print (f3(2, 3))
def f4 (x):
        print (x)
        print ("Your answer is")
        return 2*x
print (f4(2))

a = "YK"
b = 90
c = 2
def f5 (x, y, z):
        bmi = x/(y**2)
        print ("bmi:",bmi)
        if bmi > 25:
                return z + " not overweight"
        else:
                return z + " is overweight"
h = f5 (b, c, a)
print (h)


def f6 (s):
        print ("you have coverd :")
        return s*1.6 
print (f6(10))
