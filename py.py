h = 2
w = 20
bmi = w/(h**2)
print (bmi)
##average bmi is from the range of 20 to 25
if bmi > 25:
        print ("the person is over weight")
elif 20 < bmi < 25:
        print ("the person is of avg. weight")
else:
        print ("the person is under weight")
