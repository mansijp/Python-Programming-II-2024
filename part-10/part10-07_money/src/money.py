class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __str__(self):
        return f"{self.__euros+0.01*self.__cents:.2f} eur"

    def __eq__(self, another):
        string1 = self.__str__()
        string2 = another.__str__()
        return string1 == string2

    def __gt__(self, another):
        if (self.__euros+0.01*self.__cents) > (another.__euros+0.01*another.__cents):
            return True
        return False

    def __lt__(self, another):
        if (self.__euros+0.01*self.__cents) < (another.__euros+0.01*another.__cents):
            return True
        return False
    
    def __ne__(self, another):
        if (self.__euros+0.01*self.__cents) != (another.__euros+0.01*another.__cents):
            return True
        return False

    def __add__(self, another):
        return Money(self.__euros+another.__euros, self.__cents+another.__cents)
    
    def __sub__(self, another):
        if (self.__euros+0.01*self.__cents)-(another.__euros+0.01*another.__cents) < 0:
            raise ValueError("a negative result is not allowed")
        else:
            result = (self.__euros*100+self.__cents)-(another.__euros*100+another.__cents)
            return Money(result//100, result%100)

if __name__ =="__main__":
    e1 = Money(4, 5)
    e2 = Money(2, 95)

    e3 = e1 + e2
    e4 = e1 - e2

    print(e3)
    print(e4)

    e5 = e2-e1