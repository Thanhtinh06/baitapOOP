class Person:
    def __init__(self):
        self.name = ''
        self.sex = ''
        self.age = 0

    def setPerson(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def printInformationPerson(self):
        print(f"Full name: {self.name}")
        print(f"Sex: {self.sex}")
        print(f"Age: {self.age}")
