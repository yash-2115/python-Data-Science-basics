class Human:
    def __init__(self, n, o):
        self.name = n
        self.occupation = o

    def do_work(self):
        if self.occupation == "tennis player":
            print(self.name, "Playes tannis")

        elif self.occupation == "actor":
            print(self.occupation, "shoots a firm")

    def speaks(self):
        print(self.name, "says how are you ?")


tom = Human("tom crouse", "actor")
tom.do_work()
tom.speaks()


maria = Human("Maria", "tennis player")
maria.do_work()
maria.speaks()