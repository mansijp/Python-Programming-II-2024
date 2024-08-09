from collections import OrderedDict

class Task:

    unique_identifier = 1

    def __init__(self, description, workload, programmer):
        self.description = description
        self.workload = workload
        self.programmer = programmer
        self.id = Task.unique_identifier
        Task.unique_identifier += 1
        self.status = "NOT FINISHED"

    def __str__(self):
        return(f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {self.status}")
    
    def is_finished(self):
        if self.status == "FINISHED":
            return True
        return False
    
    def mark_finished(self):
        self.status = "FINISHED"

class OrderBook:

    def __init__(self):
        self.orders = []

    def add_order(self, description, workload, programmer):
        self.orders.append(Task(description, workload, programmer))

    def all_orders(self):
        order_str = []
        for order in self.orders:
            order_str.append(order)
        return order_str
    
    def programmers(self):
        programmers = []
        for order in self.orders:
            programmers.append(order.programmer)
        
        return list(OrderedDict.fromkeys(programmers))
    
    def mark_finished(self, id:int):
        if (id+1 > Task.unique_identifier) or (id+1 < 1):
            raise ValueError()
        
        for order in self.orders:
            if order.id == id:
                order.status = "FINISHED"

    def finished_orders(self):
        final = []
        for order in self.orders:
            if order.is_finished():
                final.append(order)

        return final
    
    def unfinished_orders(self):
        final = []
        for order in self.orders:
            if not order.is_finished():
                final.append(order)

        return final
    
    def status_of_programmer(self, programmer):
        if programmer not in self.programmers():
            raise ValueError()

        tup = [0, 0, 0, 0]
        for order in self.orders:
            if order.programmer == programmer:
                if order.is_finished():
                    tup[0] += 1
                    tup[2] += int(order.workload)
                else:
                    tup[1] += 1
                    tup[3] += int(order.workload)
        return (tup[0], tup[1], tup[2], tup[3])     
        # (finished tasks, unfinished tasks, finished workload, unfinished workload)

book = OrderBook()

print("commands:\n0 exit\n1 add order\n2 list finished tasks\n3 list unfinished tasks\n4 mark task as finished\n5 programmers\n6 status of programmer")

while True:
    num = int(input("\ncommand: "))
    if num == 0:
        break
    
    elif num == 1:
        desc = input("description: ")
        prog_work = input("programmer and workload estimate: ").split()

        if len(prog_work) == 1:
            print("erroneous input")
            continue
        else:
            try:
                prog_work[1] = int(prog_work[1])
            except:
                print("erroneous input")
                continue

        book.add_order(desc, prog_work[1], prog_work[0])
        print("added!")
    
    elif num == 2:
        if len(book.finished_orders()) == 0:
            print("no finished tasks")
        else:
            for task in book.finished_orders():
                print(task)

    elif num == 3:
        if len(book.unfinished_orders()) == 0:
            print("no unfinished tasks")
        else:
            for task in book.unfinished_orders():
                print(task)

    elif num == 4:
        identifier = input("id: ")
        
        try:
            identifier = int(identifier)
        except:
            print("erroneous input")
            continue
        if identifier+1 > Task.unique_identifier or identifier+1 < 1:
            print("erroneous input")
            continue

        book.mark_finished(int(identifier))
        print("marked as finished")

    elif num == 5:
        for programmer in book.programmers():
            print(programmer)

    elif num == 6:
        prog = input("programmer: ")
        
        if prog not in book.programmers():
            print("erroneous input")
            continue

        stat = book.status_of_programmer(prog)
        print(f"tasks: finished {stat[0]} not finished {stat[1]}, hours: done {stat[2]} scheduled {stat[3]}")
