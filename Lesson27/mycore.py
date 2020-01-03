class Player():
    def __init__(self, name):
        self.name = name

    def sayHelo(self):
        print("helo", self.name.title())

    def intro(self):
        print("I am player.")

class NbaPlayer(Player):
    def __init__(self, name):
        super().__init__(name)
        self.category = "nba"

    def intro(self):
        print("I am " + self.category + " player.")