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

class Myclass:
    pass

def hello():
    print("hello word!")


if __name__ == "__main__":
    A = Myclass()
    A.say = hello
    A.say()