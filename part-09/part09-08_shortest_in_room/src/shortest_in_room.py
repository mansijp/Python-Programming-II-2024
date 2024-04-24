
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name
    
class Room:
    def __init__(self):
        self.people = []
        self.combined_height = 0

    def add(self, person:Person):
        self.people.append(person)
        self.combined_height += person.height
    
    def is_empty(self):
        if(len(self.people) == 0):
            return True
        else:
            return False
    
    def print_contents(self):
        statement = f"There are {len(self.people)} in the room, and their combined height is {self.combined_height} cm"
        for p in self.people:
            statement += f"\n{p.name} ({p.height} cm)"
        print(statement)

    def shortest(self):
        shortest_height = []
        for p in self.people:
            shortest_height.append(p.height)
        if len(shortest_height) > 0:
            return(self.people[shortest_height.index(min(shortest_height))])
        else:
            return(None)
        
    def remove_shortest(self):
        if self.is_empty():
            return(None)
        else:
            shortest_person = self.people.pop(self.people.index(self.shortest()))
            return(shortest_person)

if __name__ == "main":
    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()