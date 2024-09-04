from student import Student
from professor import Professor
from lecture import Lecture

student = Student("Jonas", "Krisch", 39, ["Devops Bootcamp"])

student.get_fullname()
student.get_lectures()
student.add_lecture("DevSecOps Bootcamp")
student.get_lectures()

prof = Professor("Nana", "Janashia", "N/A", "DevOps")

prof.get_fullname()
prof.get_subjects()
prof.add_subject("Test")
prof.get_subjects()

lecture = Lecture("Devops", 50, 240, "Bob")
lecture.add_profs("Alice")
lecture.add_profs(["Joe", "Jon"])

print(lecture.list_of_profs)