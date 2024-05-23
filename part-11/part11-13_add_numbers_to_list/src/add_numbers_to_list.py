def add_numbers_to_list(num:list):
    if len(num)%5 == 0:
        return
    num.append(num[-1]+1)
    add_numbers_to_list(num)

if __name__ == "__main__":
    numbers = [1,3,4,5,10,11]
    add_numbers_to_list(numbers)
    print(numbers)