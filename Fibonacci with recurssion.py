number = int(input("enter a number: "))
def feb_series(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return feb_series(num-1) + feb_series(num-2)
for i in range(number):
    print(feb_series(i), end= " ")
