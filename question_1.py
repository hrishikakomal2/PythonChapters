class Programmer:
    compony ='microsoft'
    def __init__(self,name,product):
        self.name = name
        self.product = product
    def getInfo(self):
        print(self.name ,self.product)

hrishika = Programmer('hrishika','github')
komal = Programmer('komal','google')
hrishika.getInfo()
