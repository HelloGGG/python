def hello(strs):
    print(strs)

def request(callback):
    eval(callback)('ss')

class Test(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('initialize')


    def say(self):
        print('start')
        print(self.name, self.age)

test = Test('zero', 18)
test.say()
