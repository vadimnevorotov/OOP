class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.courses_attached = []

    def rate_lw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_attached and course in lecturer.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        delimiter = ','
        res = f'Имя: {name} + \n Фамилия: {surname} + \n Средняя оценка за домашние задания: {sum(self.grades.values()) / len(self.grades)} +\n Курсы в процессе изучения: {delimiter.join(self.courses_in_progress)} +\n Завершенные курсы: {self.finished_courses}'
        return res

    def __lt__(self, student):
        if not isinstance(student, Student):
            print(f'student is not a valid student')
        else:
            return sum(self.grades.values()) / len(self.grades) < sum(student.grades.values()) / len(student.grades)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        res = f'Имя: {name} +\n + Фамилия: {surname} + \n + Средняя оценка за лекции: {sum(self.grades.values()) / len(self.grades)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print(f'{other} is not a lecturer')
            return
        else:
            return sum(self.grades.values())/len(self.grades.values()) < sum(other.grades.values())/len(other.grades.values())


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return print(f'Имя: {name} \n Фамилия:{surname}')

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

print(best_student.grades)


