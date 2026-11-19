class Teacher:
    def __init__(self, name, subject, experience):
        self.name = name
        self.subject = subject
        self.experience = experience

    def show_info(self):
        print(f"Имя: {self.name}")
        print(f"Предмет: {self.subject}")
        print(f"Стаж: {self.experience} лет")

    def is_experienced(self):
        return self.experience >= 5
