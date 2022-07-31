# for i in range(1,11):
#     print("5 X "+ str(i) ,"=" , 5*i)
#     i = i+1

# list = ["harry","soham","sachin","rahul"]
# for name in list:
#     if name.startswith("s"):
#         print("hello, " + name)

number = int(input("enter any number  : " ))
prime = True
for i in range(2,number):
    if (number%i==0):
        prime=False
        break
if prime == False:
    print("not prime")
else:
    print("prime")



    
