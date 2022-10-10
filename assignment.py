class A :
    def __init__(self, college):
        self.college = college
class B(A):
    def __init__(self, year):
        self.year = year
class C(B):
    def __init__(self, branch):
        self.branch = branch 
class D(B):
    def __init__(self, society):
        self.society = society
class E(C,D):
    def __init__(self, name, skill):
        self.name = name
        self.skill = skill
    def details(self):
        print(f'College name : {self.college} \nYear : {self.year} \nName : {self.name} \nBranch : {self.branch} \nSociety : {self.society} \nSkills : {self.skill}')

print("Enter college name, year, name, branch, society and skills of the student")
list1 = []
for i in range(6):
    temp = input()
    list1.append(temp)
student = E(list1[2],list1[5])
student.year = list1[1]
student.college = list1[0]
student.branch = list1[3]
student.society = list1[4]

student.details()
