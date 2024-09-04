from person import Person
class Student(Person):
    def __init__(self, first_name, last_name, age, attended_lectures):
        super().__init__(first_name=first_name, last_name=last_name, age=age)
        self.attended_lectures = attended_lectures

    def get_lectures(self):
        print(self.attended_lectures)

    def add_lecture(self, lecture):
        self.attended_lectures.append(lecture)

    def remove_lecture(self, lecture):
        try:
            self.attended_lectures.remove(lecture)
        except:
            print("Could not remove lecture")