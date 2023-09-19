class Student:
    def __init__(self, name):
        self.name = name

    def print_info(self):
        print(f"{self.name} => {s.NoteInfo.model}, {s.NoteInfo.processor}, {s.NoteInfo.memory}")

    class NoteInfo:
        model = "HP"
        processor = "i7"
        memory = "16"


s = Student("Roman")
s.print_info()

s1 = Student("Vladimir")
s1.print_info()
