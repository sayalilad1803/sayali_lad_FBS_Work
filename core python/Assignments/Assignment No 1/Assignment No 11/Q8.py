num = 100

for row in range(10):
    line = []

    for i in range(10):
        line.append(num)
        num -= 1
    if row % 2 == 1:
        line.reverse()
print(line)