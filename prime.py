number = int(input("Enter a number : "))
flag = True

if number < 2 :
    print(number , "is not a prime.")
else:
    flag = True
    for i in range(2,number):
        if number % i == 0 :
            flag = False
            break
    if flag == True:
        print( number, "is a prime")
    else:
        print(number, " is not a prime.")
