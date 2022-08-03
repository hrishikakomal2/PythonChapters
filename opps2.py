class railwayForm:  # class
    formType = "railwayform"

    def printData(self):
        print(f"Name is: {self.name}")
        print(f"Train is: {self.train_name}")
        print(f"Date: {self.date}")


Application = railwayForm()   # object intantiation
Application.name = "hrishika"  #object's attributes 
Application.train_name = "gareeb rath"
Application.date = "10 aug"
Application.printData()
