def even_numbers(beginning:int, maximum:int):
    for num in range(beginning, maximum + 1):
        if num % 2 == 0:
            yield num

if __name__ == "__main__":
    numbers = even_numbers(2, 10)
    for number in numbers:
        print(number)

    numbers1 = even_numbers(11, 21)
    for number in numbers1:
        print(number)