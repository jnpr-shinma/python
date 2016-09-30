class A:
    a1 = 0
    def __init__(self, a2):
        self.a2 = a2
    def setData(self, a3):
        self.a3 = a3
    def show(self):
        print 'A1:%s,a1:%s,a2:%s,a3:%s' % (A.a1, self.a1, self.a2, self.a3)
if __name__ == '__main__':
    obj1 = A(1)
    obj2 = A(2)
    obj3 = A(3)
    obj1.setData(1)
    obj2.setData(2)
    obj3.setData(3)
    obj1.a1 = 1
    obj2.a1 = 2
    obj3.a1 = 3
    # A.a1 = 1
    A.a2 = 2
    A.a3 = 3
    obj1.show()
    obj2.show()
    obj3.show()
    print 'A1:%s,A2:%s,A3:%s' % (A.a1, A.a2, A.a3)
