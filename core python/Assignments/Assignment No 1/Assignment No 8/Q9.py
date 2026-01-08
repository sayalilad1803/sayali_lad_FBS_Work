def is_palindrome(n):
    temp = n
    rev = 0
    while n > 0:
        rev = rev * 10 + (n % 10)
        n = n // 10
    return temp == rev
num = int(input("Enter a number: "))
if is_palindrome(num):
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")