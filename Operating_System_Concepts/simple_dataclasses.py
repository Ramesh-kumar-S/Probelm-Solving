from dataclasses import dataclass, field


@dataclass
class Task:
    Name: str
    Descr: str
    ETA: str
    Priority: int
    Label: str = field(default="General")

    def print_task(self):
        print(f'{self.Name} with priority {self.Priority} has been added to the Database.')


T1 = Task("MongoDB", "Database Skill", "15/11/24", 2)
T1.print_task()
print(T1.__dict__)
print(dir(Task))
