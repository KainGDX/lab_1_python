class Student:
    def __init__(self, name, group, grades):
        self.name = name
        self.group = group
        self.grades = grades
    
    def average_grade(self):
        #считаем средний балл
        return sum(self.grades) / len(self.grades)
    
    def is_excellent(self):
        #проверяем, отличник ли студент
        return self.average_grade() >= 4.5

#читаем данные из файла
students = []
with open('students.txt', 'r', encoding='utf-8') as file:
    for line in file:
        parts = line.strip().split(';')
        name = parts[0]
        group = parts[1]
        grades = list(map(int, parts[2].split(',')))
        students.append(Student(name, group, grades))

#записываем отличников в файл
with open('excellent_students.txt', 'w', encoding='utf-8') as file:
    for student in students:
        if student.is_excellent():
            file.write(f"{student.name} - {student.group}\n")

#считаем средний балл по группам
group_grades = {}
for student in students:
    if student.group not in group_grades:
        group_grades[student.group] = []
    group_grades[student.group].append(student.average_grade())

#выводим результаты
for group, grades in group_grades.items():
    print(f"Группа {group}: средний балл {sum(grades)/len(grades):.2f}")