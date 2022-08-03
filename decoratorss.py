def dec1(func1):
    def execu():
        print("executing now")
        func1()
        print("executed")

@dec1
def dec2():
    print("i m a decorator")

dec2()