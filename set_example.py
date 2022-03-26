# Initialize the setss
set1 = {"math", 25, "banana", 49, 11, "sandwich"}
set2 = {"english", "alpha", 25, "elephant", 14}
set3 = {"english", "jamba", 49, "lemon", 27}

# This will combine multiple sets together using the .update() function

settotal = set()
for i in set1:
    for j in set2:
        for h in set3:
            settotal.update([i,j,h])
print(settotal)
