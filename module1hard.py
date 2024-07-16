# Дано:
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Решение:
# 1. Переводим множество students в список students_2.
students_2 = list (students)
print (students_2)
# 2. Сортируем список students_2 по алфавиту с помощью функции .sort. Проверяем последовательность элементов.
students_2.sort ()
print(students_2)
# 3. Вычисляем среднее арифметическое для каждого элемента списка grades.
print(sum(grades[0]) / len(grades [0]))
print(sum(grades[1]) / len(grades [1]))
print(sum(grades[2]) / len(grades [2]))
print(sum(grades[3]) / len(grades [3]))
print(sum(grades[4]) / len(grades [4]))
# 4. Составляем словарь, где ключ - имя ученика (= индекс элемента списка), а значение - средний балл ( = sum / len).
print({students_2 [0]: sum(grades[0]) / len (grades [0]),
students_2 [1]: sum(grades[1]) / len(grades [1]),
students_2 [2]: sum(grades[2]) / len(grades [2]),
students_2 [3]: sum(grades[3]) / len(grades[3]),
students_2 [4]: sum(grades[4]) / len(grades[4])})
