a = [1,2,3,4]
for e in a:
        print(e)
t = 0
for e in a:
        t += e
print (t)

x = range (1,20)
print (a)

t2 = 0
t3 = 0
for c in x:
        t2 += c
print (t2)
print (3%3)
for c in x:
        if c%3 == 0:
                t3 += c
print (t3)
t4 = 0
t5 = 0
y = range(1, 101)
for w in y:
        if w % 5 == 0:
                t4+=w
        elif w% 3 == 0:
                t5+=w
print (t4+t5)
