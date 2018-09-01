# # print(type('Hello'))
# def fn(self):
#     print('hello,world')
# Hello = type('Hello', (object,), dict(say_hello=fn))
# hello = Hello()
# hello.say_hello()

class SayMetaClass(type):
    def __new__(cls, name, bases, attrs):
        attrs['say'] = lambda self,value, name=name: print(name, value)
        return type.__new__(cls, name, bases, attrs)

class Nihao(object, metaclass=SayMetaClass):
    pass

class Hello(object, metaclass=SayMetaClass):
    pass
    
nihao = Nihao()
hello = Hello()
nihao.say('friend')
hello.say('friend')