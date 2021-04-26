class MyStuff(object):

    def __init__(self):  #调用该函数来初始化新创建的空对象
        self.tangerine = "And now a thousand years between"
        self.test = "a test" #test

    def apple(self):
        print("I am classy apples!")



thing = MyStuff()
thing.apple()
print(thing.tangerine)
print(thing.test)#test