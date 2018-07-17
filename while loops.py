total = 0
j = 0
while j<101:
        total += j
        j+=3
print (total)
a = [5,4,3,2,1]
i=0
t = 0
while i <len(a) and a[i] > 0:
        t+=a[i]
        i+=1
print (t)

b = [5,4,3,2,1,-1,-30]
y = 0
for e in b:
        if e<= 0:
            break
        y += e
        e+=1
print (y)
tx = 0
o = 0
while True:
        tx+=b[o]
        o+=1
        if b[o]<=0:
                break
print (tx)

u = [-1,-2,-3,-4]
ty = 0
q =  0
for l in b:
        if l<=0:
                ty+=l
                l+=1
print (ty)
