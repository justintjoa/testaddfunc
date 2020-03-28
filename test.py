a = 2437
b = 875
while (True):
    if (a == b):
        break
    if (a > b):
        a = a - b
    if (a < b):
        b = b - a
print(a)