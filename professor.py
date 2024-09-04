from person import Person

class Professor(Person):
    def __init__(self, first_name, last_name, age, subjects):
        super().__init__(first_name=first_name, last_name=last_name, age=age)
        if isinstance(subjects,list):
            self.subjects = subjects
        else:
            self.subjects = [subjects]


    def get_subjects(self):
        print(self.subjects)

    def add_subject(self, subject):
        self.subjects.append(subject)

    def remove_subject(self, subject):
        try:
            self.subjects.remove(subject)
        except:
            print("Could not remove subject")