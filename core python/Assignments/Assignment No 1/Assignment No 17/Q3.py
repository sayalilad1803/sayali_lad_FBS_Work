class Student:
    def __init__(self, studentId, name, age, percentage):
        self.studentId = studentId
        self.name = name
        self.age = age
        self.percentage = percentage

    def Accept(self):
        self.studentId = int(input("Enter Student ID: "))
        self.name = input("Enter Name: ")
        self.age = int(input("Enter Age: "))
        self.percentage = float(input("Enter Percentage: "))

    def Display(self):
        print("Student ID :", self.studentId)
        print("Name       :", self.name)
        print("Age        :", self.age)
        print("Percentage :", self.percentage)

    def CalculateRank(self):
        if self.percentage >= 75:
            return "Distinction"
        elif self.percentage >= 60:
            return "First Class"
        elif self.percentage >= 50:
            return "Second Class"
        elif self.percentage >= 35:
            return "Pass"
        else:
            return "Fail"

    def __str__(self):
        return f"StudentId: {self.studentId}, Name: {self.name}, Percentage: {self.percentage}"


class MedicalStudent(Student):
    
    def __init__(self, studentId, name, age, percentage, specialization, marksOfInternship):
        super().__init__(studentId, name, age, percentage)
        self.specialization = specialization
        self.marksOfInternship = marksOfInternship

    def Accept(self):
        super().Accept()
        self.specialization = input("Enter Specialization: ")
        self.marksOfInternship = float(input("Enter Internship Marks: "))

    def Display(self):
        super().Display()
        print("Specialization      :", self.specialization)
        print("Internship Marks   :", self.marksOfInternship)

    def CalculateRank(self):
        finalScore = (self.percentage + self.marksOfInternship) / 2
        if finalScore >= 75:
            return "Distinction"
        elif finalScore >= 60:
            return "First Class"
        elif finalScore >= 50:
            return "Second Class"
        elif finalScore >= 35:
            return "Pass"
        else:
            return "Fail"

    def __str__(self):
        return (f"StudentId: {self.studentId}, Name: {self.name}, "
                f"Specialization: {self.specialization}, "
                f"Percentage: {self.percentage}, "
                f"Internship Marks: {self.marksOfInternship}, "
                f"Rank: {self.CalculateRank()}")


m1 = MedicalStudent(301, "Sayali", 21, 76, "Cardiology", 85)

m1.Display()
print("Rank :", m1.CalculateRank())
print(m1)