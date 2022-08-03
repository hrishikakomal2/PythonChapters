class employee:
    company = "GOOGLE"

    def __init__(self, name, salary, subunit):  # run automatically
        print("i m a constructor!!")
        self.name = name
        self.salary = salary
        self.subunit = subunit

    def getDetail(self):
        print(self.name)
        print(self.salary)
        print(self.subunit)

    def getSalary(self, signature):
        print(
            f"the name of the employee is {self.name} and the company is {self.company} and employee salary was {self.salary} \n{signature} ")

    @staticmethod
    def greet():
        print("information")


h = employee("hrihika", 1000000000, "youtube")
h.getDetail()
