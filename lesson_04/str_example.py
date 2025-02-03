
# Multi-line string
message = """Это многостраничная 
строка.
Не веришь? 
Выведи в консоль!"""
print(message)

# Print a single character
word = "Python"
print(word[-1]) # the rightmost symbol
print(word[-6]) # sixth character from the right
# print(word[-2]) -> print(word[len(word)-2])

# string concatenation
first_name = "Виктор"
last_name = "Иванов"
full_name = first_name + last_name
print(full_name)

# string and integer concatenation
age = 25
message = "Мне " + str(age) + " лет"
print(message)

# find out the number of characters in a string
text = "Python"
print(len(text))

# Substring selection
text = "Programming"
substring = text[0:2] # Attention! Only 2 characters: Pr
print(substring)

print(text[:6]) # From 0 to 5
print(text[6:]) # From 6 to the end
print(text[6:10]) # From 6 to 9 (10 - 1)
