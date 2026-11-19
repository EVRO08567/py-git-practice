from student import Student
from teacher import Teacher

student = Student("Анна", "ИС-21", 4.8)
teacher = Teacher("Иван", "Python", 10)

student.show_info()
print("Отличник:", student.is_excellent())
print("-" * 20)
teacher.show_info()
print("Опытный преподаватель:", teacher.is_experienced())
