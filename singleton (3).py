from shutil import copytree, ignore_patterns
import os

class Singleton(type):
    """
    Define an Instance operation that lets clients access its unique
    instance.
    """

    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        print("init")
        
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        print("call")
        for arg in args:
            print(arg)
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class MyClass(metaclass=Singleton):
    """
    Example class.
    """

    pass


def main():
    #copytree(r"../../temp/present/", r"../../temp/present/pytest/", ignore=ignore_patterns('*.txt'))
    m1 = MyClass()
    m2 = MyClass()
    assert m1 is m2
    print("main")
    #m1()
    

if __name__ == "__main__":
    main()
    