import test.test


a = list(str(45654645345324502542452))

while len(a) >= 2:
    x = 0
    for i in a:
        x += int(i)
    a = list(str(x))
print(x)
