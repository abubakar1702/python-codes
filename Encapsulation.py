class Student:
    def __init__(self, name, student_id, major):
        self.name = name
        self.__student_id = student_id
        self.major = major

    def setSt_id(self, s_id):
        self.__student_id = s_id

    def getSt_id(self):
        return self.__student_id


st1 = Student("Michael Jordan", 1810745, "CSE")

st1.setSt_id(1920756)

print(st1.name)
print(st1.getSt_id())
print(st1.major)
