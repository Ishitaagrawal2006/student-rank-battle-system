class Student:
    
    def __init__(self,name, subject , marks):
        self.name = name
        self.subject = subject
        self.marks = marks
        
    def get_marks (self):
        sum = 0
        for var in self.marks:
            sum += var
        print(sum)
    def get_avg (self):
        sum = 0
        for var in self.marks:
            sum += var
        print(sum/len(self.marks)) 
stu1 = Student("TONY",["english","math","hindi"],[98,92,72])
stu2 = Student("alex",["english","math","hindi"],[85,95,60])

subjects = ["english","math","hindi"]
stu1_wins = 0
stu2_wins = 0
for i in range(3):
    if (stu1.marks[i]>stu2.marks[i]):
        print("tony win in",subjects[i])
        stu1_wins += 1
    elif (stu2.marks[i]>stu1.marks[i]):
        print("alex win in",subjects[i])
        stu2_wins += 1
    else:
        print("draw")   
if (stu1_wins > stu2_wins) :
    print("tony wins")
elif(stu2_wins > stu1_wins):
    print("alex wins")  
else:
    print("draw")                

stu1.get_avg()
stu1.get_marks()

           
    

