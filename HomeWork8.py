# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

# class Date:
#     days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#
#     def __init__(self, date):
#         self.date = date
#         self.d, self.m, self.y = map(int, date.split('-'))
#
#     @classmethod
#     def extract(cls, date):
#         date = cls(date)
#         return [date.d, date.m, date.y]
#
#     @staticmethod
#     def validate(date):
#         date = Date(date)
#         is_not_zero = date.d > 0 and date.m > 0 and date.y > 0
#         is_fit_boundaries = date.m <= 12 and date.d <= date.days_in_month[date.m - 1]
#         return is_not_zero and is_fit_boundaries
#
# date_1_valid = '02-12-1990'
# date_2_not_valid = '32-11-1991'
#
# date_1 = Date(date_1_valid)
# print(f"{date_1.extract(date_1_valid)}")
#
# date_2 = Date(date_2_not_valid)
# print(f"{date_2.extract(date_2_not_valid)}")
#
# if Date.validate(date_1_valid):
#     print(f"{date_1_valid} - корректный формат даты")
# else:
#     print(f"{date_1_valid} - некорректный формат даты")
#
# if Date.validate(date_2_not_valid):
#     print(f"{date_2_not_valid} - корректный формат даты")
# else:
#     print(f"{date_2_not_valid} - некорректный формат даты")


# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве делителя программа
# должна корректно обработать эту ситуацию и не завершиться с ошибкой.

# class Zero_divide(Exception):
#     def __init__(self, data):
#         self.d = data
#
# def program(a, b):
#     if b == 0:
#         raise Zero_divide(f'{a} / {b}, на ноль делить нельзя')
#     return a / b
#
# try:
#     program(7, 0)
# except Zero_divide as e:
#     print(e)
#
# a = int(input('Введите число: '))
# b = int(input('Введите число, отличное от 0: '))
#
# print(f"{a} / {b} = {program(a, b)}")

# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Запрашивать у пользователя данные и
# заполнять список необходимо только числами. Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно,
# пока пользователь сам не остановит работу скрипта, введя, например, команду «stop».
# При этом скрипт завершается, сформированный список с числами выводится на экран.
# Подсказка: для этого задания примем, что пользователь может вводить только числа и строки.
# Во время ввода пользователем очередного элемента необходимо реализовать проверку типа элемента.
# Вносить его в список, только если введено число. Класс-исключение должен не позволить пользователю ввести
# текст (не число) и отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.

# class Numbers(Exception):
#     def __init__(self, data):
#         self.d = data
#
# def is_it_number(string):
#     if string.isdigit():
#         return string
#     else:
#         return Numbers(f'Ошибка: {string} не является числом')
#
# input_txt = ''
# count = 1
# list = []
# print("Введите числа по одному. Для выхода из программы введите 'stop'")
# while input_txt != 'stop':
#     try:
#         input_txt = input(f"{count}: ")
#         list.append(is_it_number(input_txt))
#         count += 1
#     except Numbers as e:
#         if input_txt != 'stop':
#             print(e.txt)
#
# print(f'Список:\n{list}')

# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.

# class Sklad:
#
# class Orgtechnika:
#     def __init__(self, name, model, year):
#         self.name = name
#         self.model = model
#         self.year = year
#
#     def __repr__(self):
#         return f'{self.name}-{self.model}-{self.year}'
#
# class Printer(Orgtechnika):
#     def __init__(self, series, name, model, year):
#         super().__init__(name, model, year)
#         self.series = series
#
#     def action(self):
#         return 'Печатает'
#
# class Xerox(Orgtechnika):
#     def __init__(self, name, model, year):
#         super().__init__(name, model, year)
#
#     def action(self):
#         return 'Копирует'
#
# class Scaner(Orgtechnika):
#     def __init__(self, name, model, year):
#         super().__init__(name, model, year)
#
#     def action(self):
#         return 'Сканирует'


# 5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и
# передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру (например, словарь).

# class Sklad:
#     def __init__(self):
#         self.dict = {}
#
#     def add_to(self, equipment):
#         self.dict.setdefault(equipment.name, []).append(equipment)
#
#     def extract(self, name):
#         if self.dict[name]:
#             self.dict.setdefault(name).pop(0)
#
# class Orgtechnika:
#     def __init__(self, name, model, year):
#         self.name = name
#         self.model = model
#         self.year = year
#
#     def __repr__(self):
#         return f'{self.name}-{self.model}-{self.year}'
#
# class Printer(Orgtechnika):
#     def __init__(self, series, name, model, year):
#         super().__init__(name, model, year)
#         self.series = series
#
#     def action(self):
#         return 'Печатает'
#
# class Xerox(Orgtechnika):
#     def __init__(self, name, model, year):
#         super().__init__(name, model, year)
#
#     def action(self):
#         return 'Копирует'
#
# class Scaner(Orgtechnika):
#     def __init__(self, name, model, year):
#         super().__init__(name, model, year)
#
#     def action(self):
#         return 'Сканирует'
#
# sklad = Sklad()
# scaner = Scaner('Samsung','M1', 2003)
# sklad.add_to(scaner)
# scaner = Scaner('HP','S2', 2018)
# sklad.add_to(scaner)
# scaner = Scaner('Shimazu','Harakiri', 2021)
# sklad.add_to(scaner)
# print(sklad.dict)
# sklad.extract('Shimazu')
# print(sklad.dict)


# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
# для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

# class Sklad:
#     storage = []
#     summary = {}
#
#     def __init__(self):
#         self.dict = {}
#
#     def push(self, orgtechnic):
#         if not isinstance(orgtechnic, Orgtechnika):
#             raise Exception('Склад только для оргтехники')
#         self.storage.append(orgtechnic)
#         if self.summary.get(orgtechnic.name) is not None:
#             self.summary[orgtechnic.name] += 1
#         else:
#             self.summary.setdefault(orgtechnic.name, 1)
#
#     def report_items(self):
#         for item in self.storage:
#             print(item)
#
#     def report_total(self):
#         for k, v in self.summary.items():
#             print(f'{k}: {v} шт')
#
#     def add_to(self, equipment):
#         self.dict.setdefault(equipment.name, []).append(equipment)
#
#     def extract(self, name):
#         if self.dict[name]:
#             self.dict.setdefault(name).pop(0)
#
# class Orgtechnika:
#     def __init__(self, name, model, year):
#         self.name = name
#         self.model = model
#         self.year = year
#
#     def __repr__(self):
#         return f'{self.name}-{self.model}-{self.year}'
#
# class Printer(Orgtechnika):
#     def __init__(self, series, name, model, year):
#         super().__init__(name, model, year)
#         self.series = series
#
#     def action(self):
#         return 'Печатает'
#
# class Xerox(Orgtechnika):
#     def __init__(self, name, model, year):
#         super().__init__(name, model, year)
#
#     def action(self):
#         return 'Копирует'
#
# class Scaner(Orgtechnika):
#     def __init__(self, name, model, year):
#         super().__init__(name, model, year)
#
#     def action(self):
#         return 'Сканирует'
#
# sklad = Sklad()
# printer_1 = Printer(1213, 'Samsung','M1', 2003)
# sklad.add_to(printer_1)
# scaner_1 = Scaner('HP','S2', 2018)
# sklad.add_to(scaner_1)
# xerox_1 = Xerox('Shimazu','Harakiri', 2021)
# sklad.add_to(xerox_1)
# print(sklad.dict)
# sklad.extract('Shimazu')
# print(sklad.dict)
#
# Sklad().push(printer_1)
# Sklad().push(scaner_1)
# Sklad().push(xerox_1)
#
# Sklad().report_items()
# Sklad().report_total()

# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
# Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

# class Complex_number:
#     def __init__(self, a, b, *args):
#         self.a = a
#         self.b = b
#         self.z = 'a + b * i'
#
#     def __add__(self, other):
#         print(f'Сумма z1 и z2 равна')
#         return f'z = {self.a + other.a} + {self.b + other.b} * i'
#
#     def __mul__(self, other):
#         print(f'Произведение z1 и z2 равно')
#         return f'z = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'
#
#     def __str__(self):
#         return f'z = {self.a} + {self.b} * i'
#
#
# z_1 = Complex_number(2, -3)
# z_2 = Complex_number(3, -5)
# print(z_1)
# print(z_1 + z_2)
# print(z_1 * z_2)