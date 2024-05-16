class ListHelper:

    @classmethod
    def greatest_frequency(cls, my_list:list):
        freq = {}
        for i in my_list:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        
        greatest_freq = 0
        result = 0
        for key in freq:
            if freq[key] > greatest_freq:
                result = key
                greatest_freq = freq[key]
        
        return(result)
    
    @classmethod
    def doubles(cls, my_list:list):
        freq = {}
        for i in my_list:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        
        doubles = 0
        for key in freq:
            if freq[key] >= 2:
                doubles += 1

        return(doubles)
    
if __name__ == "main":
    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))


