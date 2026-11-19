class Student:
    def __init__(self, name, group, average_grade):
        self.name = name
        self.group = group
        self.average_grade = average_grade

    def show_info(self):
        print(f"Имя: {self.name}")
        print(f"Группа: {self.group}")
        print(f"Средний балл: {self.average_grade}")

    def is_excellent(self):
        return self.average_grade >= 4.5
