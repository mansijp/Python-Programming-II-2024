class SimpleDate:

    def __init__(self, day:int, month:int, year:int):
        self.__day = day
        self.__month = month
        self.__year = year

    def __str__(self):
        return f"{self.__day}.{self.__month}.{self.__year}"
    
    def __eq__(self, another: object):
        if self.__day == another.__day and self.__month == another.__month and self.__year == another.__year:
            return True
        return False
    
    def __ne__(self, another:object):
        if self.__day != another.__day or self.__month != another.__month or self.__year != another.__year:
            return True
        return False
    
    def __gt__(self, another:object):
        if self.__year > another.__year:
            return True
        elif self.__year == another.__year and self.__month > another.__month:
            return True
        elif self.__year == another.__year and self.__month == another.__month and self.__day > another.__day:
            return True
        return False
    
    def __lt__(self, another:object):
        if self.__year < another.__year:
            return True
        elif self.__year == another.__year and self.__month < another.__month:
            return True
        elif self.__year == another.__year and self.__month == another.__month and self.__day < another.__day:
            return True
        return False
    
    def __add__(self, another:int):
        yearInc = another // 360
        monthInc = another%360 // 30
        dayInc = another%360%30
       
        # increment year
        newYear = self.__year + yearInc
        # increment month
        if self.__month + monthInc > 12:
            newMonth = self.__month + monthInc - 12
            newYear += 1
        else:
            newMonth = self.__month + monthInc
        # day increment
        if self.__day + dayInc > 30:
            newDay = self.__day + dayInc - 30
            newMonth += 1
        else:
            newDay = self.__day + dayInc
        
        return SimpleDate (newDay, newMonth, newYear)
    
    def __sub__(self, another:object):
        startDays = self.__day + self.__month*30 + self.__year*360
        endDays = another.__day + another.__month*30 + another.__year*360
        return(abs(endDays - startDays))

if __name__ == "__main__":    
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(28, 12, 1985)

    d3 = d1 + 3
    d4 = d2 + 400

    print(d1)
    print(d2)
    print(d3)
    print(d4)

    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(2, 11, 2020)
    d3 = SimpleDate(28, 12, 1985)

    print(d2-d1)
    print(d1-d2)
    print(d1-d3)