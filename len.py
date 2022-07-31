name = input("enter your name : ")
if(len(name) >10):
    print(" your name is more than 10 character : ")
    name =int(len(name))
    # name=int(name)
    print("your name's length is : ",name)

else:
    print("welcome, " + name )
