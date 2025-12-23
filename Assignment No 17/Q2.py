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


class EnggStudent(Student):
    
    def __init__(self, studentId, name, age, percentage, branch, internalMarks):
        super().__init__(studentId, name, age, percentage)
        self.branch = branch
        self.internalMarks = internalMarks

    def Accept(self):
        super().Accept()
        self.branch = input("Enter Branch: ")
        self.internalMarks = float(input("Enter Internal Marks: "))

    def Display(self):
        super().Display()
        print("Branch     :", self.branch)
        print("Internal Marks :", self.internalMarks)

    def CalculateRank(self):
        avg = (self.percentage + self.internalMarks) / 2
        if avg >= 75:
            return "Distinction"
        elif avg >= 60:
            return "First Class"
        elif avg >= 50:
            return "Second Class"
        elif avg >= 35:
            return "Pass"
        else:
            return "Fail"

    def __str__(self):
        return (f"StudentId: {self.studentId}, Name: {self.name}, "
                f"Branch: {self.branch}, "
                f"Percentage: {self.percentage}, "
                f"InternalMarks: {self.internalMarks}, "
                f"Rank: {self.CalculateRank()}")


e1 = EnggStudent(201, "Sayali", 21, 78, "Computer", 82)

e1.Display()

print("Rank :", e1.CalculateRank())

print(e1)