class Clock:
    def __init__(self, h, m, s):
        self.hours = h
        self.minutes = m
        self.seconds = s

    def tick(self):
        if self.hours == 23 and self.minutes == 59 and self.seconds == 59:
            self.hours = 0
            self.minutes = 0
            self.seconds = 0
        elif self.minutes == 59 and self.seconds == 59:
            self.hours += 1
            self.minutes = 0
            self.seconds = 0
        elif self.seconds == 59:
            self.minutes += 1
            self.seconds = 0
        else:
            self.seconds += 1
    
    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"
    
    def set(self, new_hours, new_minutes):
        self.seconds = 0
        if new_minutes >= 0 and new_minutes <= 59:
            self.minutes = new_minutes
        if new_hours >= 0 and new_hours <= 23:
            self.hours = new_hours
    
if __name__ == "__main__":
    clock = Clock(23, 59, 55)
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)

    clock.set(12, 5)
    print(clock)

