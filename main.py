class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

    def lect_gr(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]

        else:
            return 'Ошибка'

    def __add__(self):
        sum_grade = 0
        all_gr = best_student.grades.get('Python')
        a = len(all_gr)
        for grd in all_gr:
            sum_grade += grd
        result = ((sum_grade)/a)
        return float(result)


    def gr(self, course):
        sum_gr = 0
        all_grad = self.grades.get(str(course))
        a = len(all_grad)
        for grd in all_grad:
            sum_gr += grd
        result = ((sum_gr)/a)
        return float(result)


    def bst_stud(self, best_st, course):
        if not isinstance(best_st, Student):
             pass
        if best_st.gr(course) < self.gr(course):
            return f'Студент {self.name} {self.surname} лучше, чем {best_st.name} {best_st.surname} по курсу {course}'

        elif best_st.gr(course) > self.gr(course):
            return f'Студент {best_st.name} {best_st.surname} лучше, чем {self.name} {self.surname}'
        else:
            return ('Студенты равны')



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
        return f'Имя: {self.name}\nФамилия: {self.surname}'

    def __add__(self):
        sum_gr = 0
        all_gr = cool_lecturer.grades.get('Python')
        a = len(all_gr)
        for gr in all_gr:
            sum_gr += gr
        result = ((sum_gr)/a)
        return float(result)

    def gr(self,course):
        sum_gr = 0
        all_gr = self.grades.get(course)
        a = len(all_gr)
        for gr in all_gr:
            sum_gr += gr
        result = ((sum_gr)/a)
        return float(result)


    def bst_lect(self, best_lc,course):
        if not isinstance(best_lc, Lecturer):
             pass
        if best_lc.gr(course) < self.gr(course):
            return f'Лектор {self.name} {self.surname} лучше, чем {best_lc.name} {best_lc.surname} по курсу {course}'
            # best_lc.status = 'Этот лектор хуже'
            # self.status = 'Этот лектор лучше'
        elif best_lc.gr(course) > self.gr(course):
            return f'Лектор {best_lc.name} {best_lc.surname} лучше, чем {self.name} {self.surname} по курсу {course}'
        else:
            return ('Лекторы равны')


class Reviewer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'



if __name__ == '__main__':

    cool_mentor = Mentor('Some', 'Buddy')
    cool_mentor.courses_attached += ['Python']

    cool_reviewer = Reviewer('Some', 'Buddy')
    cool_reviewer.courses_attached += ['Python']
    some_reviewer = Reviewer('Some', 'Buddy')

    cool_lecturer = Lecturer('Some', 'Buddy')
    cool_lecturer.courses_attached += ['Python']
    some_lecturer = Lecturer('Some', 'Buddy')
    ivanov = Lecturer('Александр', 'Иванов')
    ivanov.courses_attached += ['Python']
    petrov = Lecturer('Иван', 'Петров')
    petrov.courses_attached += ['Python']
    sidorov = Lecturer('Петр', 'Сидоров')
    sidorov.courses_attached += ['Python']


    best_student = Student('Ruoy', 'Eman', 'your_gender')
    some_student = Student('Ruoy', 'Eman', 'your_gender')
    std_aleksandr = Student('Александр', 'Пушкин', 'муж')
    std_aleksandr.courses_in_progress += ['Python', 'Git']
    std_mihail = Student('Михаил', 'Лермонтов', 'муж')
    std_mihail.courses_in_progress += ['Python', 'Git']
    std_anna = Student('Анна', 'Ахматова', 'жен')
    std_anna.courses_in_progress += ['Python', 'Git']
    best_student.courses_in_progress += ['Python', 'Git']
    best_student.finished_courses += ['Введение в программирование']
    best_student.lect_gr(cool_lecturer, 'Python', 10)
    best_student.lect_gr(cool_lecturer, 'Python', 9)
    best_student.lect_gr(cool_lecturer, 'Python', 8)
    best_student.lect_gr(cool_lecturer, 'Python', 7)

    best_student.lect_gr(petrov, 'Python', 8)
    best_student.lect_gr(petrov, 'Python', 9)
    best_student.lect_gr(petrov, 'Python', 9)
    best_student.lect_gr(petrov, 'Python', 7)

    best_student.lect_gr(ivanov, 'Python', 6)
    best_student.lect_gr(ivanov, 'Python', 6)
    best_student.lect_gr(ivanov, 'Python', 9)
    best_student.lect_gr(ivanov, 'Python', 10)


    cool_reviewer.rate_hw(best_student, 'Python', 10)
    cool_reviewer.rate_hw(best_student, 'Python', 10)
    cool_reviewer.rate_hw(best_student, 'Python', 10)

    cool_reviewer.rate_hw(std_aleksandr, 'Python', 10)
    cool_reviewer.rate_hw(std_aleksandr, 'Python', 8)
    cool_reviewer.rate_hw(std_aleksandr, 'Python', 7)

    cool_reviewer.rate_hw(std_mihail, 'Python', 10)
    cool_reviewer.rate_hw(std_mihail, 'Python', 10)
    cool_reviewer.rate_hw(std_mihail, 'Python', 9)

    cool_reviewer.rate_hw(std_anna, 'Python', 10)
    cool_reviewer.rate_hw(std_anna, 'Python', 10)
    cool_reviewer.rate_hw(std_anna, 'Python', 10)


    print(best_student.grades)
    print(cool_lecturer.grades)
    print()
    print(some_reviewer)
    print()
    print(some_lecturer)
    print(f'Средняя оценка за лекции: {some_lecturer.__add__()}')
    print()
    print(some_student)
    print(f'Средняя оценка за домашние задания: {some_student.__add__()}')
    print(f'Курсы в процессе изучения: {best_student.courses_in_progress}')
    print(f'Завершенные курсы: {best_student.finished_courses}')
    print()
    print(ivanov.bst_lect(petrov, 'Python')) # Сравнеие лекторов
    print()
    print(std_mihail.bst_stud(std_aleksandr, 'Python')) #Сравнение студентов



