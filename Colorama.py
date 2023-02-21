import colorama
import inspect
import  sys

# Ім'я бібліотеки

# print(colorama.__name__)

# Ім'я модуля

# print(__name__)

# Тип об'єкта

# print(type(colorama))

# Атрибути та методи

# for method in dir():
#     print(method)

# Перевірка наявності атрибута чи метода в класі

# data = "string"
# print(hasattr(data, "index"))
# print(hasattr(data, "reverse"))

# Дізнатися чи можна викликати об'єкт

# data = "string"
# def first_function():
#     pass
# print(callable(first_function))
# print(callable(data))

# Дізнатися чи успадковується клас

# class Class1:
#     pass
# class Class2(Class1):
#     pass
# print(issubclass(Class1, Class2))
# print(issubclass(Class2, Class1))

# Дізнатися чи належить об'єкт певному класу

# class Class1:
#     pass
# class Class2(Class1):
#     pass
#
# obj_from_class_2 = Class2()
# print(isinstance(obj_from_class_2, Class1))
# print(isinstance(obj_from_class_2, Class2))

# Дізнатися чим являється об'єкт

# print(inspect.ismodule(colorama))
# print(inspect.isclass(colorama))
# print(inspect.isfunction(colorama))

# Повертання назви модуля

# print(inspect.getmodule(colorama.get))
# print(inspect.getmodule(list))

# Дослідження об'єкту

# class Human:
#     def __init__(self, age, height, name="Tim"):
#         self.age = age
#         self.name = name
#         self.secondname = "Wick"
#
# sig = inspect.signature(Human)
# for parametr in sig.parameters.values():
#     print(parametr.name,parametr.default)

# Місце знаходження інтерпритатора Python

# print(sys.executable)

# Версія інтерпритатора Python

# print(sys.version)

# Данні операційної сис-ми

# print(sys.platform)

# Розміщення модулю

# print(sys.argv)

# Дізнатися назву всіх імпортованих модудів і шляхи до них

# for module_name, module_path in sys.modules.items():
#     print(module_name, module_path)

# Усі вбудованні данні

# for _ in dir(__builtins__):
#     print(_)


