for i in range(1, 6):
    for j in range(1, 6-i):
        print(' ', end=' ')

    num = i

    for j in range(i):
        print(num, end=' ')
        num +=1
    num -= 2

    for j in range(i - 1):
        print(num, end=' ')
        num -=1

    print()

    

        