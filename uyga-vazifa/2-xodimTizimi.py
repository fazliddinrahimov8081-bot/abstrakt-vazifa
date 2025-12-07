class Employee:
    def __init__(self, name: str, employee_id: str, hourly_rate: float = 15.0):
        self.name = name
        self.employee_id = employee_id
        self.hourly_rate = hourly_rate
        self.__working_hours = []  # private list
        print(f"Xodim yaratildi: {self.name}, ID: {self.employee_id}, stavka: {self.hourly_rate}")

    def log_hours(self, hour: int) -> bool:
        # Soat faqat 0–24 oralig‘ida bo‘lishi shart
        if 0 <= hour <= 24:
            self.__working_hours.append(hour)
            return True
        return False

    def total_hours(self) -> int:
        return sum(self.__working_hours)

    def calculate_salary(self) -> float:
        return self.total_hours() * self.hourly_rate

    def reset_hours(self) -> None:
        self.__working_hours.clear()
employee = Employee("Javlon", "E101", hourly_rate=20.0)

print(employee.log_hours(8))     # True
print(employee.log_hours(9))     # True
print(employee.log_hours(10))    # True
print(employee.log_hours(25))    # False

print(employee.total_hours())         # 27
print(employee.calculate_salary())    # 540.0

employee.reset_hours()
print(employee.total_hours())         # 0
print(employee.calculate_salary())    # 0.0
