#  -*- coding:utf-8 -*-
# 元类，改变产生的类的行为和语意


class TypedProperty(object):

    def __init__(self, type, default=None):
        self.name = None
        self.type = type
        self.default = default if default else type()

    def __get__(self, instance, cls):
        return getattr(instance, self.name, self.default)

    def __set__(self, instance, value):
        if not isinstance(value, self.type):
            raise TypeError("Must be a %s" % self.type)

        setattr(instance, self.name, value)
    
    def __delete__(self, instance):
        raise AttributeError("Can't delete attribute")


class TypedMeta(type):
    
    def __new__(cls, name, bases, class_dict): # 创建一个实例对象
        slots = []
        for key, value in class_dict.items():
            if isinstance(value, TypedProperty):
                value.name = '_' + key
                slots.append(value.name)
        class_dict['__slots__'] = slots
        return type.__new__(cls, name, bases, class_dict)


class Typed(metaclass=TypedMeta):
    pass


class Foo(Typed):
    name = TypedProperty(str)
    num = TypedProperty(int, 42)
