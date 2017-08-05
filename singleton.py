"""
Ensure a class only has one instance, and provide a global point of
access to it.
"""
from icp import *
from isp import * 
import logging

class boger:
    i=9
    def __init__(self):
        self.i=8

class Terry(boger):
    def __init__(self):
        self.i = 10
        print(super())
        print("terry")

class Singleton(type):
    """
    Define an Instance operation that lets clients access its unique
    instance.
    """
    def __init__(cls, name, bases, attrs, **kwargs):
        print(super())
        print(cls.__class__)
        print(cls.__class__.__class__)

        logging.basicConfig(filename="d.log", level=logging.INFO)
        logging.info("Singleton init")
        print("iinti")
        super().__init__(name, bases, attrs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        print(cls)
        print("ccall")
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance

#class Programmer:
class Programmer(metaclass=Singleton):
    def __init__(self, strategy):
        _icp = ICP()
        _isp = ISP()
        if strategy == "usb_swd":
            self._strategy = _icp
        elif strategy == "usb":
            self._strategy = _isp
        elif strategy == "uart":
            self._strategy = _isp

        print("init programmer only once")
        print(strategy)
    def connect(self):
        self._strategy.connect_func()

    def start(self):
        #self._strategy.erase_func()
        self._strategy.prog_func()

    def set_strategy(self, strategy):
        self._strategy = strategy


def main():
    t = Terry()
    print(t.i)
    b = boger()
    print(b.i)
    print(boger.i)
    m1 = MyClass()
    #m2 = MyClass()
    #assert m1 is m2
    print(t.__class__)
#print(type(1))
#print(type("ss"))
#print(type({1,}))
#print(Terry)
#print(type(Terry))
#print(Terry.__class__)
#print(Singleton)
#print(type(Singleton))
#print("------------")
#print(type)
#print(super(MyClass))


if __name__ == "__main__":
    main()
