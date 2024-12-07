import random
a = int(input("Enter a num : "))
b = int(input("Enter a num : "))
z =[]
for i in range(a, b):
    z.append(random.randint(a,b))
y = random.choices(z)
print(y)