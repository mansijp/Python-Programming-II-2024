
class Course:
    def __init__(self, name:str, grade:int, credits:int):
        self.__name = name
        self.__grade = grade
        self.__credits = credits

    def name(self):
        return self.__name
    def grade(self):
        return self.__grade
    def credits(self):
        return self.__credits
    
    def __str__(self):
        return f"{self.__name} ({self.__credits} cr) grade {self.__grade}"
    
class CourseRecords:
    def __init__(self):
        self.__courses = {}

    def add_course(self, name, grade, credits):
        if name in self.__courses:
            if self.__courses[name].grade() < grade:
                self.__courses[name] = Course(name, grade, credits)
        else:
            self.__courses[name] = Course(name, grade, credits)
    
    def get_course_data(self, name):
        if name in self.__courses:
            print(self.__courses[name])
        else:
            print("no entry for this course")

    def statistics(self):
        completed_courses = 0
        total_credits = 0
        total_grade = 0
        grade_freq = [0, 0, 0, 0, 0]
        
        for i in self.__courses:
            completed_courses += 1
            total_credits += int(self.__courses[i].credits())
            total_grade += int(self.__courses[i].grade())
            grade_freq[int(self.__courses[i].grade())-1] += 1

        res = f"{completed_courses} completed courses, "
        res += f"a total of {total_credits} credits"
        res += f"\nmean {round(total_grade/completed_courses, 1)}"
        res += f"\ngrade distribution"

        for g in range(len(grade_freq), 0, -1):
            res += f"\n{g}: " + "x"*grade_freq[g-1]
        
        return res

class CourseRecordsApp:
    def __init__(self):
        self.__record = CourseRecords()
    
    def commands(self):
        print("1 add course\n2 get course data\n3 statistics\n0 exit")

    def add_course(self):
        course = input("course: ")
        grade = input("grade: ")
        credits = input("credits: ")
        self.__record.add_course(course, grade, credits)

    def get_course_data(self):
        course = input("course: ")
        self.__record.get_course_data(course)
    
    def statistics(self):
        print(self.__record.statistics())

    def run(self):
        self.commands()
        choice = -1
        while True:
            choice = input("\ncommand: ")
            if choice == "0":
                return
            if choice == "1":
                self.add_course()
            if choice == "2":
                self.get_course_data()
            if choice == "3":
                self.statistics()

app = CourseRecordsApp()
app.run()
        