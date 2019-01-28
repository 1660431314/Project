class bird(object):

    def getAge(self):
        if age < 1 :return 1
        else : return age
    def setAge(self,value):
        if value > 2 : value = 2
        self.age = value
    age = property(getAge,setAge)


b = bird()
b.setAge(3)
print (b.getAge)
