class Example(object):
    def __init__(self, num):
        self.num = num

    def get_arg(self):
        return self.num

    def set_arg(self, arg):
        self.num = arg


e = Example(5)
print(e.get_arg())
e.set_arg(10)
print(e.get_arg())
