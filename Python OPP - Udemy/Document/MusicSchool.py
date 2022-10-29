
class MusicSchool:

    students = {"Gino":   [15, "653-235-345", ["Piano", "Guitar"]],
                                                "Talina": [28, "555-765-452", ["Cello"]],
                                                "Eric":   [12, "583-356-223", ["Singing"]]}

    def __init__(self, working_hours, revenue):
        self.working_hours = working_hours
        self.revenue = revenue
    
    
    def print_student(self,name_student):
        students = self.students
        age_student = students[name_student][0]
        classes = students[name_student][2]
        print(f'{name_student} who is {age_student} year old and is taking {classes}')

    def print_student_data(self):
        students = self.students
        for name in students.keys():
            self.print_student(name)            
        
    def add_student(self,name,data):
        self.students[name] = data
        file = open("new_student_information.txt", "w")
        file.write()
        

            
                              
# Create the instance
my_class = MusicSchool(8,1000)


# Call the methods
# print(my_class.print_student_data())
my_class.print_student_data()
my_class.add_student('Voi',[20,'0943165280',['Guitar']])



