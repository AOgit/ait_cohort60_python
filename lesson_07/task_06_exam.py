# Напишите функцию, которая определяет, сдал ли студент экзамен, и возвращает True,
# если сдал, и False – если не сдал.
# Для успешной сдачи экзамена студенту необходимо иметь два зачёта,
# а также получить балл не ниже 80 на самом экзамене.
# Функция имеет три параметра – сдан ли первый зачёт, сдан ли второй зачёт,
# полученный балл на экзамене.
# Вызовите функцию несколько раз, передав ей различные аргументы, и выведите результаты в консоль.

def is_exam_passed(is_test1_passed: bool, is_test2_passed: bool, grade: int) -> bool:
    return is_test1_passed and is_test2_passed and grade >= 80

print(is_exam_passed(True, False, 80))
print(is_exam_passed(False, False, 80))
print(is_exam_passed(True, True, 80))
print(is_exam_passed(True, True, 70))


