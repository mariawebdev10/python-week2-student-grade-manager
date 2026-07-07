class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 90:
            return "A+"
        elif self.marks >= 80:
            return "A"
        elif self.marks >= 70:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 50:
            return "D"
        else:
            return "Fail"

    def display(self):
        print("\n----- Student Information -----")
        print("Name :", self.name)
        print("Roll No :", self.roll_no)
        print("Marks :", self.marks)
        print("Grade :", self.calculate_grade())