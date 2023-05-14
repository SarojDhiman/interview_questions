class Student:
    '''here is the main class or parent class'''
    def __init__(self,x,y):
        self.x=x
        self.y=y
        print("here i define the variables or parameters that i have")
class Teacher(Student):
    print("here i inherit the pparent class in child")

class Yellow(Student):
    def bright_student(self):
        print("this finally inherit",self.x,self.y)

class private(Yellow):
    def __this(self,v,__th):
        self.v = 4
        self.__th=7
        print(self.v)
        print(self.__th)

o1 = Student(4,5)
o1.x
o2 = Teacher(5,6)
o2.y
o3=private(4,5)
o3._private__this(5,6)
