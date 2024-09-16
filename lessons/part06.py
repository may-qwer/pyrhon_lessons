# class Temp:
#     name = "Temp"
#
#     def __init__(self, n):
#         self.nickname = n
#
#     def make_name(self):
#         Temp.name = Temp.name + self.nickname
#
#
# if __name__ == "__main__":
#     green = Temp("green")
#     print(green.nickname)
#     print(green.name)
#     green.make_name()
#     print(green.name)
#     print(Temp.name)

# class Myclass:
#     pass
#
# def hello():
#     print("hello word!")
#
#
# if __name__ == "__main__":
#     A = Myclass()
#     A.say = hello
#     A.say()

# class BoxSize:
#     def __init__(self, w, h, d):
#         self.w = w
#         self.h = h
#         self.d = d
#
#     def calculate_volume(self):
#         return self.w*self.h*self.d
#
#
# class BoxParams:
#     def __init__(self, weight, color):
#         self.weight = weight
#         self.color = color
#
#
# class Box(BoxSize, BoxParams):
#     def __init__(self, w, h, d, weight, color):
#         BoxSize.__init__(self, w, h, d)
#         BoxParams.__init__(self, weight, color)
#
#     def __str__(self):
#         return str(self.calculate_volume()) + "\n" + str(self.weight) + " " + str(self.color)
#
#
#
# if __name__ == "__main__":
#     box = Box(10, 1, 23, 5, "red")
#     print(box)

class Vector:
    def __init__(self, a=0, b=0, c=0):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return "V = <" + str(self.a) + ", " + str(self.b) + ", "  + str(self.c) + ">"

    def __add__(self, x):
        return Vector((self.a + x.a), (self.b + x.b), (self.c + x.c))

    def __radd__(self, x):
        return Vector((self.a + x.a), (self.b + x.b), (self.c + x.c))

    def __sub__(self, x):
        return Vector((self.a - x.a), (self.b - x.b), (self.c - x.c))

    def __rsub__(self, x):
        return Vector((self.a - x.a), (self.b - x.b), (self.c - x.c))

    def __mul__(self, x):
        if type(x) == Vector:
            return Vector((self.a * x.a), (self.b * x.b), (self.c * x.c))
        elif type(x) == int:
            return Vector((self.a * x), (self.b * x), (self.c * x))

    def __rmul__(self, x):
        if type(x) == Vector:
            return Vector((self.a * x.a), (self.b * x.b), (self.c * x.c))
        elif type(x) == int:
            return Vector((self.a * x), (self.b * x), (self.c * x))

    def __truediv__(self, x):
        try:
            return Vector((self.a / x), (self.b / x), (self.c / x))
        except ZeroDivisionError:
            return "Cannot be divided by zero"

    def __abs__(self):
        return int(self.a**2 + self.b**2 + self.c**2)


if __name__ == "__main__":
    v1 = Vector(1, 2, 4)
    v2 = Vector(5, 6, 7)

    print(v1 + v2)
    print(v1 - v2)
    print(v1 * 2)
    print(v1 * v2)
    print(v1 / 2)
    print(v2 / 0)
    print(abs(v1))

