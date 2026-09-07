class school:
    def study(self):
        print("Children study in school")
class staff(school):
    def work(self):
        print("staff works")
class students(school,staff):
    def read(self):
        print("Student reads")
d1=students()
d1.study()
d1.work()
d1.read()