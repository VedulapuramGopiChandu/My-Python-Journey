li = ["dog", "cat", "cat", "fox", "rat", "dog"]
count = 0
counted_strings = set()
for str in li:
    if str not in counted_strings:
        num = li.count(str)
        print(str, num)
        counted_strings.add(str)
    


    
