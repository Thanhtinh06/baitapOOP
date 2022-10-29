class People:
    def __init__(self):
        self.name = ''
        self.sex = ''
        self.age = 0

    def setPeople(self):
        self.name = input()
        self.sex = input()
        self.age = input()

    def getInformationPeople(self):
        print(f"Full name: {self.name}")
        print(f"Sex: {self.sex}")
        print(f"Age: {self.age}")
