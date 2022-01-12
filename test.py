class Yo():
    myName = "Kenny"

    def __str__(self):
        return self.myName + '22'


obj = Yo()
print(obj)
print(obj.myName)