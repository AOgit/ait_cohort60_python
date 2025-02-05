
# 0. () - скобки
# 1. not
# 2. and
# 3. or

print(False and False)
print(True or False)
print(True or False and False) # False and False -> True or True -> True
print(True or False and not True) # True -> True or False and False -> True or False -> True

# Логическое "И"
print("True and True:", True and True) # True
print("True and False:", True and False) # False
print("False and True:", False and True) # False
print("False and False:", False and False) # False

print("True or True:", True or True) # True
print("True or False:", True or False) # True
print("False or True:", False or True) # True
print("False or False:", False or False) # False

# Логическое YT
print("not (10 > 5):", not (10 > 5)) # not True -> False
# not False = True