class Father(object):
    def money(self):
        print("Father has 20W")
class Son(Father):
    def money(self):
        print("son get 10w from father")
        super(Son,self).money()
        print("super value")

dad = Father()
son = Son()

dad.money()
son.money()