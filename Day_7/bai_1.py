class Pycon:
    id = 1
    def __init__(self, name, age, job):
        self.id = Pycon.id
        self.name = name
        self.age = age
        self.job = job
        Pycon.id += 1
    
    def nhap(self):
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))
        
    @classmethod
    def averAge(cls, pycons):
        return sum([pycon.age for pycon in pycons]) / len(pycons)
    
    def __str__(self) -> str:
        return f'ID: {self.id}, Tên: {self.name}, Tuổi: {self.age}'
    

pycons = []
n = int(input("Enter the number of Pycons: "))

for _ in range(n):
    pycon = Pycon('', 0, '')
    pycon.nhap()
    pycons.append(pycon)

print("\n\n")
for pycon in pycons:
    print(pycon)
print(f'Average age: {Pycon.averAge(pycons)}')
print("\n\n")