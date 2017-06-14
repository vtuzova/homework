"""
Попробуйте перенести в ОО-код следующий пример из реального мира:
- есть курсы, учителя и ученики
- у каждого курса есть свой учитель
- у каждого учителя есть своя группа учеников

Определите какие объекты есть в этом примере, какие у них свойства и какие
методы, как эти объекты будут между собой взаимодействовать, например, к курсу
можно добавить учителя.
"""

#класс Учитель, которому можно назначать те или иные группы студентов
class Teacher(object):
    def __init__ (self, teacher, students_group):
        self.teacher = teacher
        self.students_group = []


        if students_group is not None:
            for p in students_group:
                self.add_students_group(p)


    def add_students_group(self, students_group):
        self.students_group.append(students_group)


teacher1 = Teacher('Буравчик А.И.', ('group1-1', 'group1-2'))
teacher2 = Teacher('Тартаковская И.А.', ('group1-1',))
teacher2.add_students_group('group3-1',)
            
tch1 = [teacher1.teacher, teacher1.students_group]
tch2 = [teacher2.teacher, teacher2.students_group]


#класс Курс, которому можно назначать того или иного преподавателя
class Course(object):
    def __init__ (self, name, teacher=None):
        self.name = name
        self.teacher = []
        
        if teacher is not None:
            for p in teacher:
                self.add_teacher(p)

    def add_teacher(self, teacher):
        self.teacher.append(teacher)

    def get_info(self): 
        return ('{}, преподаватель: {}').format(
            self.name,
            self.teacher,
        )
  
           

course1 = Course('физика', tch1)
course2 = Course('история', tch2)
course2.add_teacher(tch1)

print('course_1:', Course.get_info(course1))
print('course_2:', Course.get_info(course2))


    
    
    





    
