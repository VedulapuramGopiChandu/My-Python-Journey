dic = {"names":["gopi","sai", "phani", "dhana"]}
print(dic)

res = {values: keys  for keys in dic for values in dic[keys]}
print(res)