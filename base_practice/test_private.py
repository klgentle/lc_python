class TestPrivate(object):
    def __init__(self, name):
        self.__name = name

    def get_value(self):
        return self.__name


#a = TestPrivate("Cklll")
#print(a.get_value())


class pub():
    _name = 'protected类型的变量'
    __info = '私有类型的变量'
    def _func(self):
        print("这是一个protected类型的方法")
    def __func2(self):
        print('这是一个私有类型的方法')
    def get(self):
        return(self.__info)

a = pub()
print(a.get())
