my_list = [1, 2, 3]
c = map( lambda i: i * i, my_list )
print(list(c))
print(my_list)

def add100(x):
    return x + 100

#map(add100,my_list)

print([add100(i) for i in my_list])


def deco(func): 
    def call_method(*args): 
        print ("before call method" )
        func(*args) 
        print ("after call method" )
    return call_method 

@deco 
def func(a,b): 
    print ("in func" )
    return a + b 
    
func(1,2)

def is_persistent(_self):
    return False

print(id (my_list))

class Some:
    def __new__(clz, isClzInstance):
        print('__new__')
        if isClzInstance:
            print(object)
            return object.__new__(clz)
        else:
            return None
    def __init__(self, isClzInstance):
        print('__init__')
        print(isClzInstance)
Some(True)
print(Some)
print(hasattr(Some, 'gg'))
Some.gg=is_persistent
print(hasattr(Some, 'gg'))
s=Some(False)
ss=Some(False)
print(Some.gg)
#print(ss.gg)

    
def Persistent(klass):
    """
    类的decorator，用来修饰Entity的子类。如：
    @Persistent
    class player(Entity):
        ...
    这样的类才会被序列化到mongodb中
    """
    klass.is_persistent = is_persistent
    return klass
 
@Persistent
class player(object): #object is Entity above
    pass
    
pp=player()
print(pp.is_persistent())   #print false


class Singleton:
    __single = None
    def __new__(clz):
        print("ggggg")
        print(clz)
        print(object)
        if not Singleton.__single:
            Singleton.__single = object.__new__(clz)
        return Singleton.__single

    def __init__(clz):
        print("initttt")
        #print(clz)
        
    def doSomething(self):
        pass
        #print(self)

singleton1 = Singleton()
singleton1.doSomething()
print(singleton1)

class Chain(object):
    def __init__(self, path=''):
        self._path = path
    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))
    def __str__(self):
        return self._path
    __repr__ = __str__

print(Chain().status.user.timeline.list)

