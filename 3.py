def palindrome (a):
    x = (len(a))
    x = x-1
    print (x)
    if a[0] == a[x]:
        x = x-1
        if a[1] == a[x]:
            print ("it is a palidrome")
    else:
        print ("It is not a Palindrome")

palindrome ("race car")
