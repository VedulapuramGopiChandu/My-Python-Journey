num = int(input("Enter a number: "))
n1 = 0
n2 = 1
sum = 0
for i in range(num):
    print(sum, end = " ")
    n1 = n2
    n2 = sum
    sum = n1 + n2
print(sum)
