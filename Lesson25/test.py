class Player():
    def __init__(self, name):
        self.name = name

    def sayHelo(self):
        print("helo", self.name.title())

    def intro(self):
        print("I am player.")

curry = Player("curry")
print(curry.name)
curry.sayHelo()
curry.intro()

james = Player("james")
print(james.name)
james.sayHelo()
james.intro()