class car:
    maxspeed = 0
    name = ""
    def __init__(self):
        self.maxspeed = 200
        self.name = "Supercar"
    def drive(self):
        print(self.maxspeed)
car1 = car()
car1.drive()
car1.maxspeed = 10
car1.drive()
