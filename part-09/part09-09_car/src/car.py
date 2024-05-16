class Car:
    def __init__(self):
        self.__petrol = 0
        self.__km = 0
    
    def __str__(self):
        return(f"Car: odometer reading {self.__km} km, petrol remaining {self.__petrol} litres")

    def fill_up(self):
        self.__petrol = 60
    
    def drive(self, km:int):
        if(km > self.__petrol):
            self.__km += self.__petrol
            self.__petrol = 0
        else:
            self.__km += km
            self.__petrol -= km

if __name__ == "main":
    car = Car()
    print(car)
    car.fill_up()
    print(car)
    car.drive(20)
    print(car)
    car.drive(50)
    print(car)
    car.drive(10)
    print(car)
    car.fill_up()
    car.fill_up()
    print(car)