class Accelerate:
    def __init__(self, newspeed, oldspeed):
        self.newspeed = newspeed
        self.oldspeed = oldspeed

    def adjustspeed(self):
        print(f"Car will accelerate from {self.oldspeed} to {self.newspeed}")


class Deccelerate:
    def __init__(self, newspeed, oldspeed):
        self.newspeed = newspeed
        self.oldspeed = oldspeed

    def adjustspeed(self):
        print(f"Car will deccelerate from {self.oldspeed} to {self.newspeed}")





accelerate1 = Accelerate(50,25)
accelerate2 = Accelerate(60,50)
deccelerate1 = Deccelerate(30,60)


for adjustment in (accelerate1, accelerate2, deccelerate1):
    adjustment.adjustspeed()