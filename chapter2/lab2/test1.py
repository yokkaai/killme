
# завдання2

# a = input("Введіть число: ")
# assert a.isdigit(), "Потрібно ввести число!"
# print(f"введене число: {a}")

# завдання 3-4:


# class Figure:
#     def __init__(self, type, length) -> None:
#         assert length > 0, "Довжина має бути більшою за 0!"
#         assert type in ["квадрат", "прямокутник",
#                         "трикутник"], "Дозволені фігури: квадрат, прямокутник, трикутник"
#         self.type = type
#         self.length = length


# try:
#     a = Figure("трапеція", 9)
# except AssertionError as e:
#     print(e)

# try:
#     b = Figure("квадрат", 0)
# except AssertionError as e:
#     print(e)

# try:
#     c = Figure("квадрат", 1)
#     print(f"Фігура створена: {c.type} з довжиною {c.length}")
# except AssertionError as e:
#     print(e)


# 6 завдання
# class Name:
#     def __init__(self, name, hobby) -> None:
#         # Перевірка імені
#         if name not in ["Богдан", "Анонім", "sofia"]:
#             raise ValueError("Дозволені імена: Богдан, Анонім, sofia")

#         # Перевірка хобі
#         if not hobby:
#             raise ValueError("Хобі не може бути порожнім!")

#         self.name = name
#         self.hobby = hobby


# try:
#     a = Name("Бодько", "шахи")
# except ValueError as e:
#     print(e)

# try:
#     b = Name("sofia", "")
# except ValueError as e:
#     print(e)

# try:
#     c = Name("sofia", "шахи")
#     print(f"Фігура створена: {c.name}, Хобі: {c.hobby}")
# except ValueError as e:
#     print(e)