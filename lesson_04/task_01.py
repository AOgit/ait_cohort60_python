storage_width = int(input("Введите ширину склада: "))
storage_length = int(input("Введите длину склада: "))
storage_height = int(input("Введите высоту склада: "))

box_width = int(input("Введите ширину коробки: "))
box_length = int(input("Введите длину коробки: "))
box_height = int(input("Введите высоту коробки: "))

storage_volume = storage_height * storage_length * storage_width
box_volume = box_height * box_length * box_width

amount_boxes = storage_volume // box_volume

print("На склад поместится", amount_boxes, "столов")
print(f"На склад поместится {storage_volume/box_volume:.0f} столов ")
