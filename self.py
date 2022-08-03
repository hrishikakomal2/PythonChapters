class employee:
    company ="GOOGLE"
    def getSalary(self):  #self is a parameter pass automatically when object is called. use-- we use instance attibutes as well as class attributes .
        print("100k")

h = employee()
h.getSalary()
employee.getSalary(h) # == h.getSalary()