while True:
    a = int(input("Enter your 1st number:-"))
    b = int(input("Enter your 2nd number:"))
    c = "Now code for the operations are/n 1-Addition/n 2-Subtraction/n 3-Multiplication/n 4-Division/n 5-Floor Division/n 6-Modulo/n 7-Power"
    d = int(input("Enter your code for specific operation"))
    e = a+b
    f = a-b
    g = a*b
    h = a/b
    i = a//b
    j = a%b
    k = a**b
    if d==1:
        print("The result is ", e)
    elif d==2:
        print("The result is ", f)
    elif d == 3:
        print("The result is ", g)
    elif d == 4:
         print("The result is ", h)
    elif d == 5:
        print("The result is ",i)
    elif d == 6:
        print("The result is ",j)
    elif d==7:
        print("The result is ",k)
    else:
        break