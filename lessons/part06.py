class Temp:
    name = "Temp"

    def __init__(self, n):
        self.nickname = n

    def make_name(self):
        Temp.name = Temp.name + self.nickname


if __name__ == "__main__":
    green = Temp("green")
    print(green.nickname)
    print(green.name)
    green.make_name()
    print(green.name)
    print(Temp.name)