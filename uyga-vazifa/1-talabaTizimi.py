class Student:
    def __init__(self, name: str, student_id: str):
        self.name = name
        self.student_id = student_id
        self.__grades = []   # private list
        print(f"Yangi talaba yaratildi: {self.name}, ID: {self.student_id}, baholar ro'yxati bo'sh.")

    def add_grade(self, grade: int) -> None:
        # 0–100 oraliqda bo‘lmasa — xato
        if not (0 <= grade <= 100):
            print("Xato: Noto'g'ri baho")
            return
        
        self.__grades.append(grade)
        print(f"{grade} bahosi qo'shildi.")

    def calculate_average(self) -> float:
        if len(self.__grades) == 0:
            return 0
        return sum(self.__grades) / len(self.__grades)

    def get_status(self) -> str:
        avg = self.calculate_average()

        if 90 <= avg <= 100:
            return "A'lo"
        elif 80 <= avg < 90:
            return "Yaxshi"
        elif 70 <= avg < 80:
            return "Qoniqarli"
        else:
            return "Qoniqarsiz"
student = Student("Nodira", "S123")

student.add_grade(85)
student.add_grade(90)

print(student.calculate_average())  # 87.5
print(student.get_status())         # Yaxshi

student.add_grade(150)  # Xato: Noto'g'ri baho
