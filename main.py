# class Test:
#
#     pas = 7
#
#     @staticmethod # статический метод, не ссылается на объекты
#     def m1():
#         return 'Car has gone'
#
#     def m2(self): # обычный метод
#         return f'Car has {self.pas} seats'
#
#     @classmethod
#     def m3(cls, new):
#         cls.pas = new
#
#
# car1 = Test()
#
# print(car1.m2())
# Test.m3(12)
#
# car2 = Test()
# print(car2.m2())

class Worker:
    def __init__(self, name, sur):
        self.n = name
        self.s = sur
        print(f'name: {self.n}, surname: {self.s}')

    @classmethod
    def set_fio(cls, data):
        n, s = data
        return cls(n, s)

    @staticmethod
    def get_fio(obj):
        return f'name: {obj.n}, surname: {obj.s}'


li = ['Tom', 'Madson']
# w = 'Tom' - 'Hudson' - 2000
# w1 = Worker(li[0], li[1])
w1 = Worker.set_fio(li)