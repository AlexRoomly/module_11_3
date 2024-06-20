class Robot:
    def __init__(self, name=None):
        if name:
            self.name = name
        else:
            self.name = 'R2D2'

    def hello(self):
        print('Привет мир! Я -', self.name)

    def go(self, x=10, y=10):
        print('иду в точку', x, y)


robot = Robot()


def some_function(param, param_2='n/a'):
    print('my params is', param, param_2)


# Тип объекта.
# Атрибуты объекта.
# Методы объекта.
# Модуль, к которому объект принадлежит.
# Другие интересные свойства объекта, учитывая его тип (по желанию).
# {'type': 'int', 'attributes': ['__abs__', '__add__', ...], 'methods': [],
# 'module': '__main__'}

def introspection(obj):
    objDict = {}
    objDict.setdefault('type', type(obj))
    attributes = dir(obj)
    obj_atr = []
    obj_met = []
    for method in attributes:
        if callable(getattr(obj, method)):
            obj_met.append(method)
        else:
            obj_atr.append(method)
    objDict.setdefault('attributes', obj_atr)
    objDict.setdefault('methods', obj_met)
    try:
        if obj.__module__:
            objDict.setdefault('module', obj.__module__)
        if obj.__name__:
            objDict.setdefault('name', obj.__name__)
    except AttributeError:
        return objDict
    return objDict


number_info = introspection(42)
print(number_info)

number_info = introspection('red')
print(number_info)
number_info = introspection(robot)
print(number_info)

number_info = introspection(some_function)
print(number_info)
