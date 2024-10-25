grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = list(students)              # переводим множество в список
students_list.sort()                        # сортируем по алфавиту

grades_a0 = sum(grades[0]) / len(grades[0]) # расчитываем среднеарифметическое по каждому ученику
grades_b1 = sum(grades[1]) / len(grades[1])
grades_c2 = sum(grades[2]) / len(grades[2])
grades_d3 = sum(grades[3]) / len(grades[3])
grades_e4 = sum(grades[4]) / len(grades[4])
grades_list = [grades_a0, grades_b1, grades_c2, grades_d3, grades_e4]

dict = {}                                   # делаем выборку значений из списков учеников и оценок в общий словарь
for key in students_list:
    for value in grades_list:
        dict[key] = value
        grades_list.remove(value)
        break
print('' + str(dict))