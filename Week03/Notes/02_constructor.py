# WEEK 3 - CONSTRUCTOR

class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

student1 = Student("Milind", 21, "B.Tech AIML")

print(student1.name)
print(student1.age)
print(student1.course)