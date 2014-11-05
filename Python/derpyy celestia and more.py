class pony:

    name = "Princess Celestia"
    color = "pink"

    def walk(self):
        print("See?  I am walking. -says " + self.name)
    def talk(self):
        print("my name is " + self.name + " and my color is " + self.color)


p = pony()
print(p.name)
p.walk()
t = p
t.name = "Derpy"
print(p.name)
p.walk()
p.color = "Gray"
p.talk()
