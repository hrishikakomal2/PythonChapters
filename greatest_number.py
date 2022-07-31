a = int(input("enter the number : "))
b = int(input("enter the number : "))
c = int(input("enter the number : "))
d = int(input("enter the number : "))
# if(a>b and a>c and a>d ):
#     print(a," is greatest")
# elif(b>c and b>d):
#     print(b," is greatest")
# elif(c>d):
#     print(c," is greatest")
# else:
#     print(d," is greatest")

if(a>d):
    number = a
else:
    number = d
if(b> c):
    number1 = b
else:
    number1 = c
if(number > number1):
    print(number," is greater among all")
else:
    print(number1,"is greater among all ")


