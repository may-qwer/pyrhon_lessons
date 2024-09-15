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

class BoxSize:
    def __init__(self, w, h, d):
        self.w = w
        self.h = h
        self.d = d

    def calculate_volume(self):
        return self.w*self.h*self.d


class BoxParams:
    def __init__(self, weight, color):
        self.weight = weight
        self.color = color


class Box(BoxSize, BoxParams):
    def __init__(self, w, h, d, weight, color):
        BoxSize.__init__(self, w, h, d)
        BoxParams.__init__(self, weight, color)

    def __str__(self):
        return str(self.calculate_volume()) + "\n" + str(self.weight) + " " + str(self.color)



if __name__ == "__main__":
    box = Box(10, 1, 23, 5, "red")
    print(box)