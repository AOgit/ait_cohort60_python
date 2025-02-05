# Напишите функцию, которая проверяет на корректность адрес электронной почты,
# и возвращает True, если адрес корректен, и False – если нет.
# Функция имеет один параметр – адрес электронной почты.
# Представим, что адрес корректен, если:
# он не менее 8 символов в длину,
# содержит «@»,
# содержит точку и
# не содержит «#».
# Вызовите функцию несколько раз, передав ей различные аргументы, и выведите результаты в консоль.

def is_valid_email(text):
    return len(text) >= 8 and "@" in text and "." in text and not "#" in text

print(is_valid_email("sdsdf@gmail.com"))
print(is_valid_email("sdfsdf.sdfru"))
print(is_valid_email("sdf#.sdfru"))
print(is_valid_email("sd@gm.de"))
