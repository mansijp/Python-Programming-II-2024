class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.numbers_list = []

    def add_number(self, number:int):
        self.numbers_list.append(number)        
        self.numbers += 1

    def count_numbers(self):
        return(self.numbers)
    
    def get_sum(self):
        if self.numbers == 0:
            return (0)
        return(sum(self.numbers_list))

    def average(self):
        if self.numbers == 0:
            return(0)
        return(sum(self.numbers_list)/self.numbers)

print("Please type in integer numbers:")
stats = NumberStats()
statsEven = NumberStats()
statsOdd = NumberStats()

tempNum = int(input(""))
while(tempNum != -1):
    stats.add_number(tempNum)
    if(tempNum % 2 == 0):
        statsEven.add_number(tempNum)
    elif(tempNum % 2 == 1):
        statsOdd.add_number(tempNum)
    tempNum = int(input(""))

print("Sum of numbers:", stats.get_sum())
print("Mean of numbers:", stats.average())
print("Sum of even numbers:", statsEven.get_sum())
print("Sum of odd numbers:", statsOdd.get_sum())
