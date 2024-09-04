class Lecture:
    def __init__(self, name, max_number_of_students, duration, list_of_profs):
        self.name = name
        self.max_number_of_students = max_number_of_students
        self.duration = duration
        if isinstance(list_of_profs,list):
            self.list_of_profs = list_of_profs
        else:
            self.list_of_profs = [list_of_profs]

    def get_name_and_duration(self):
        print(f"lecture: {self.name}, duration: {self.duration}")

    def add_profs(self, professors):
        if isinstance(professors, list):
            for prof in professors:
                self.list_of_profs.append(prof)
        else:
            self.list_of_profs.append(professors)