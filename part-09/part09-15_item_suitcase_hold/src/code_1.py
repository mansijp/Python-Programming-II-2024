class Item:
    def __init__(self, name:str, weight:int):
        self.__name = name
        self.__weight = weight

    def name(self):
        return (self.__name )

    def weight(self):
        return (self.__weight)

    def __str__(self):
        return(f"{self.__name} ({self.__weight} kg)")
    
class Suitcase:

    def __init__(self, max_weight:int):
        self.__maxWeight = max_weight
        self.__items = []
        self.__total_weight = 0
    
    def add_item(self, item:Item):
        if(self.__total_weight + item.weight() <= self.__maxWeight):
            self.__items.append(item)
            self.__total_weight += item.weight()

    def __str__(self):
        if (len(self.__items) == 1):
            return(f"{len(self.__items)} item ({self.__total_weight} kg)")
        return(f"{len(self.__items)} items ({self.__total_weight} kg)")
    
    def print_items(self):
        for i in self.__items:
            print(i)

    def weight(self):
        return(self.__total_weight)
    
    def items(self):
        return(self.__items)

    def heaviest_item(self):
        item_weights = []
        for item in self.__items:
            item_weights.append(item.weight())

        return(self.__items[item_weights.index(max(item_weights))])

class CargoHold:
    def __init__(self, maxWeight:int):
        self.__maxWeight = maxWeight
        self.__suitcases = []
        self.__cargoWeight = 0

    def add_suitcase(self, suitcase:Suitcase):
        if (suitcase.weight() + self.__cargoWeight <= self.__maxWeight):
            self.__suitcases.append(suitcase)
            self.__cargoWeight += suitcase.weight()

    def __str__(self):
        if (len(self.__suitcases) == 1):
            return(f"{len(self.__suitcases)} suitcase, space for {self.__maxWeight - self.__cargoWeight} kg")
        return(f"{len(self.__suitcases)} suitcases, space for {self.__maxWeight - self.__cargoWeight} kg")

    def print_items(self):
        for s in self.__suitcases:
            for i in s.items():
                print(i)

if __name__ == "__main__":
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()