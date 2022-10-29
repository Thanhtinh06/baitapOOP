class Student:
  
    def classes(self,class_of_student):
        self.class_of_student = class_of_student
      


class ClassOfStudent:

    def __init__(self,code, start_time, end_time, class_assigned):
        self.class_code = code
        self.start_time = start_time
        self.end_time = end_time
        self.class_assigned = class_assigned
        
        
class ToDoList:

    def __init__(self):
        self.personal = None
        self.work = None
        self.academic = None
        self.leisure = None
    
    
    def status_of_to_do_list(self):
      pass
        
        
        