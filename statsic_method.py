class employee:
    company = "GOOGLE"

    def getSalary(self, signature):
        print(
            f"the name of the employee is {self.name} and the company is {self.company} and employee salary was {self.salary} \n{signature} ")

    @staticmethod
    def greet():
        print("information")


h = employee()
h.greet()
h.name = "hrishika"
h.salary = '1 CR'
h.getSalary("thnks!!")
# employee.getSalary(h) # == h.getSalary()
