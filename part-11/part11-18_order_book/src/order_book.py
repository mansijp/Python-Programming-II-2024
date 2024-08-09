class Task:

    unique_identifier = 1

    def __init__(self, description, programmer, workload):
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
        my_list = []
        for order in self.orders:
            my_list.append(order.programmer)
        
        programmers = list(set(my_list))
        return programmers
    
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
    
    def status_of_programmer(self, programmer:str):
        if programmer not in self.programmers():
            raise ValueError()

        tup = [0, 0, 0, 0]
        for order in self.orders:
            if order.programmer == programmer:
                if order.is_finished():
                    tup[0] += 1
                    tup[2] += order.workload
                else:
                    tup[1] += 1
                    tup[3] += order.workload
        return (tup[0], tup[1], tup[2], tup[3])

