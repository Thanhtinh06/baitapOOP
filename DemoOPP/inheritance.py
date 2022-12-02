# from abc import abstractmethod

# class Animal:
#     def __init__(self) -> None:
#         self.foot = "foot"
    
#     @abstractmethod
#     def tiengkeu():
#       pass
    
# class Dog(Animal):
#     def __init__(self) -> None:
#         super().__init__()
#         self.tail = Tail()
#     #override lai abstract of base class 
#     def tiengkeu():
#       print("gaugau")

# #Horse is composite. 1 components is Tail
# class Horse(Animal):
#     def __init__(self) -> None:
#         super().__init__()
#         self.tail = Tail()
    
#     def tiengkeu():
#        print("")
        
# class Tail():
#     def __init__(self) -> None:
#       self.activies = ''
#     def wave():
#       print("wave")
      
# A Python program to demonstrate inheritance
#(object -> có thể có hoặc không)
# class Person(object):

#     # Constructor
#     def __init__(self, name, id):
#       self.name = name
#       self.id = id

#     # To check if this person is an employee
#     def Display(self): #method
#       print(self.name, self.id)


# # Driver code
# emp = Person("Satyam", 102) # An Object of Person
# emp.Display()

# Python code to demonstrate how parent constructors
# are called.

# parent class
class Person(object):

	# __init__ is known as the constructor
	def __init__(self, name, idnumber):
		self.name = name
		self.idnumber = idnumber

	def display(self):
		print(self.name)
		print(self.idnumber)

# child class


class Employee(Person):
	def __init__(self, name, idnumber, salary, post):
		self.salary = salary
		self.post = post

		# invoking the __init__ of the parent class
		Person.__init__(self, name, idnumber)


# creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")

# calling a function of the class Person using its instance
a.display()



