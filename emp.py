# list = "hello hi Wellcome to Python world"

# li= list.split(" ")
# li
# # for char in enumerate(li):
# #     print(li)

# dict = {char : list.count(char) for char in list}
# d = sorted(dict)
# print(d)


p = {"lap": 1000, "phon": 800, "car": 100, "bike": 700}
d = {keys : values for keys , values in p .items() if values > 500 }
print(d)