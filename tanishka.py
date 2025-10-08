num = int(input("Enter a number: "))
x=0
while num>0:
    d=num%10
    print("Reminder:",d)
    x=x*10+d
    print("Reversed so far:",x)
    num=num//10
print("Final reversed number:",x)
