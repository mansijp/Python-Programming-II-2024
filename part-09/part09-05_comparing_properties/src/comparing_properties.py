class RealProperty:
    def __init__(self, rooms: int , square_metres: int , price_per_sqm:int):
        self.rooms = rooms
        self.square_metres = square_metres
        self.price_per_sqm = price_per_sqm

    def bigger(self, compared_to):
        if compared_to.square_metres > self.square_metres:
            return (False)
        return(True)
    
    def price_difference(self, compared_to):
        compared_to_price = compared_to.price_per_sqm * compared_to.square_metres
        self_price = self.price_per_sqm * self.square_metres
        return(abs(compared_to_price - self_price))
    
    def more_expensive(self, compared_to):
        if self.price_per_sqm*self.square_metres > compared_to.price_per_sqm*compared_to.square_metres:
            return(True)
        return(False)

if __name__ == "main":
    central_studio = RealProperty(1, 16, 5500)
    downtown_two_bedroom = RealProperty(2, 38, 4200)
    suburbs_three_bedroom = RealProperty(3, 78, 2500)

    print(central_studio.more_expensive(downtown_two_bedroom))
    print(suburbs_three_bedroom.more_expensive(downtown_two_bedroom))