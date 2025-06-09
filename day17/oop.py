class Details:
    colleg_name = "Balkumari College"
    
    # def __init__(self):
    #     print("default constructors")
        
    #parameterize constructors
    def __init__(self, fullname, marks):
        self.name = fullname
        self.marks = marks
        print("----- Student Details list ----- ")

    def welcome(self):
        print("Welcome Student" , self.name , self.marks)
    
    def get_marks(self):
        return self.marks

student_One = Details("Nishan Kumar Rai", 47)
# print(student_One.name)
# print(student_One.colleg_name)
student_One.welcome()