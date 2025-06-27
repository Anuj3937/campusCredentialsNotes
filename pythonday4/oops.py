class microWave():
    def __init__(self,brandName,powerRating,price) ->str :
        self.brandName=brandName
        self.powerRating=powerRating
        self.price=price
        self.turnOn = False
    def turnedOn(self) -> str:
        if self.turnOn == False:
            self.turnOn = True
            return (f"your microwave {self.brandName} is now turned on")
        else:
            return (f"your microwave {self.brandName} is already turned on")
    def run(self,seconds):
        if self.turnOn:
            print(f"{self.brandName} is running for {seconds}")
        else:
            print("it is off , turn it on first")
    def __add__(self,other) -> None:
        return f" {self.brandName} + {other.brandName}"
    def __str__(self):
        return f"{self.brandName} has a price of {self.price} and a power rating of {self.powerRating}"
    def __repr__(self):
        return "repr"
    