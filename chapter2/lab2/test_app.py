# class Figure:
#     FIGURES = ["квадрат", "прямокутник", "трикутник"]

#     def __init__(self, type, length) -> None:
#         assert length > 0, "Довжина має бути більшою за 0!"
#         assert type in self.FIGURES, "Дозволені фігури: квадрат, прямокутник, трикутник"
#         self.type = type
#         self.length = length

#     @property
#     def get_figure_type(self):
#         return self.type

#     @property
#     def get_figure_length(self):
#         return self.length


# # Створення об'єктів
# try:
#     a = Figure("квадрат", 4)
#     print(f"Тип фігури: {a.get_figure_type}, Довжина: {a.get_figure_length}")
# except AssertionError as e:
#     print(e)

# try:
#     b = Figure("трикутник", 5)
#     print(f"Тип фігури: {b.get_figure_type}, Довжина: {b.get_figure_length}")
# except AssertionError as e:
#     print(e)

# try:
#     c = Figure("коло", 7)
# except AssertionError as e:
#     print(e)

# try:
#     d = Figure("квадрат", 0)
# except AssertionError as e:
#     print(e)


# class Figure:
#     FIGURES = ["квадрат", "прямокутник", "трикутник"]

#     def __init__(self, type, length) -> None:
#         assert length > 0, "Довжина має бути більшою за 0!"
#         assert type in self.FIGURES, "Дозволені фігури: квадрат, прямокутник, трикутник"
#         self.type = type
#         self.length = length

#     @property
#     def get_figure_type(self):
#         return self.type

#     @property
#     def get_figure_length(self):
#         return self.length  # виправлено на правильне значення (повертати довжину)

# import unittest
# from random import choice, randint
# from app import Figure  # імпорт класу Figure з app.py

# import unittest
# from random import choice, randint


# class TestFigure(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         """Виконується лише раз на початку тестів"""
#         pass

#     def setUp(self) -> None:
#         """Виконується кожного разу, коли запускається тест"""
#         self.figure = choice(Figure.FIGURES)  # Вибір випадкової фігури
#         self.length = randint(1, 10)  # Випадкова довжина від 1 до 10
#         self.obj = Figure(self.figure, self.length)
#         super().setUp()

#     def tearDown(self) -> None:
#         """Виконується після кожного тесту"""
#         del self.obj
#         super().tearDown()

#     def test_figure_type(self):
#         self.assertEqual(self.figure, self.obj.get_figure_type(),
#                          "Метод get_figure_type повертає неправильну фігуру!")

#     def test_figure_length(self):
#         self.assertEqual(self.length, self.obj.get_figure_length(),
#                          "Метод get_figure_length повертає неправильну довжину!")

#     def test_invalid_figure(self):
#         with self.assertRaises(ValueError):
#             Figure("коло", 1)


# class Figure:
#     FIGURES = ["квадрат", "прямокутник", "трикутник"]

#     def __init__(self, type, length) -> None:
#         assert length > 0, "Довжина має бути більшою за 0!"
#         assert type in self.FIGURES, "Дозволені фігури: квадрат, прямокутник, трикутник"
#         self.type = type
#         self.length = length

#     @property
#     def get_figure_type(self):
#         return self.type

#     @property
#     def get_figure_length(self):
#         return self.length

# # Тест для створення фігури типу "трикутник"
# def test_app_triangle():
#     """Test if we create triangle figure."""
#     fig = "трикутник"
#     triangle = Figure(fig, 4)
#     assert triangle.type == fig, f"Фігура має бути {fig}"


# class Figure:
#     FIGURES = ["квадрат", "прямокутник", "трикутник"]

#     def __init__(self, type, length) -> None:
#         assert length > 0, "Довжина має бути більшою за 0!"
#         assert type in self.FIGURES, "Дозволені фігури: квадрат, прямокутник, трикутник"
#         self.type = type
#         self.length = length

#     @property
#     def get_figure_type(self):
#         return self.type

#     @property
#     def get_figure_length(self):
#         return self.length

#     @property
#     def get_angles(self):
#         if self.type in ["квадрат", "прямокутник"]:
#             return 4
#         if self.type == "трикутник":
#             return 3


# def test_get_angles():
#     """Тестуємо чи правильно повертається кількість кутів фігури."""
#     fig = "трикутник"
#     triangle = Figure(fig, 1)
#     assert triangle.get_angles == 3, f"У {fig} є 3 кути!"

#     fig = "квадрат"
#     square = Figure(fig, 1)
#     assert square.get_angles == 4, f"У {fig} є 4 кути!"

#     fig = "прямокутник"
#     rectangle = Figure(fig, 1)
#     assert rectangle.get_angles == 4, f"У {fig} є 4 кути!"