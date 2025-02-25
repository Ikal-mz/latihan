class A:

    def show(self):
        print('ini adalah show A')

class B:

    def show(self):
        print('ini adalah show B')

class C:

    def show(self):
        print('ini adalah show C')

class D(B,C):
    pass

objek = D()
objek.show()