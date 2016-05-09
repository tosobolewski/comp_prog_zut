# zad 3 lista 1 programowanie obiektowe

class Rectangle:

    def __init__(self, sideA, sideB):
        self.sideA = sideA
        self.sideB = sideB

    def area(self):
        return self.sideA * self.sideB

def showRect(rect):
    print(rect.sideA, rect.sideB, rect.area())

def test():
    pass

def main():
    r = Rectangle(10, 5)
    r2 = Rectangle(30, 12)
    r3 = Rectangle(15, 18)

    rectList = []
    for el in [r, r2, r3]:
        rectList.append(el)

    for el in rectList:
        print(el.area())

    for el in rectList:
        showRect(el)


if __name__ == '__main__':
    test()
    main()

