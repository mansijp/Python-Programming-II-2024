class Recording:

    def __init__(self, len):
        if len < 0:
            raise ValueError
        else:
            self.length = len

    def __str__(self):
        return(self.__length)
    
    # length getter method
    @property
    def length(self):
        return self.__length
    
    # length setter method
    @length.setter
    def length(self, length):
        if length < 0:
            raise ValueError
        else:
            self.__length = length

if __name__ == "main":
    the_wall = Recording(43)
    print(the_wall.length)
    the_wall.length = -1
    print(the_wall.length)