# Q3 WAP to reverse a number (eg. 123456 -> 654321)

num = int(input("Enter a number: "))
rev_num = 0
while num > 0:
    digit = num % 10
    rev_num = rev_num * 10 + digit
    num //= 10
print(f"The reversed number is: {rev_num}")