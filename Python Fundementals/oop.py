class myClass():
    def method1(self):
        print("Z-Digital Group")
    
    def method2(self, string_parameter):
        print("Hello", string_parameter)

class childClass(myClass):
    def method1(self):
        myClass.method1(self)
        print("is cool!")

    def method2(self):
        print("This is a message from a child Class")

class User():
    name = ""

    def __init__(self, name):
        self.name = name

    def sayHello(self):
        print("Hello", self.name)

def main():
    c = childClass()
    c.method1()
    c.method2()

    u = User("Bohdan")
    u.sayHello()

if __name__ == "__main__":
    main()