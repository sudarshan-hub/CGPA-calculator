#CGPA calculator
import itertools
import os
import sys

#Subject and credits list
Sem1={'Calculus and its Applications':4, 'Physics':3, 'Chemistry of Electronic materials':3,
      'Problem solving and C programming':2, 'Electrical Engineering Drawing':2,
      'Problem solving and C programming Laboratory':1, 'English language proficiency':3 }
Sem2={'Basic Sciences laboratory':2, 'Complex variables and transforms':4, 'Semiconductor devices':3,
      'Applied electrochemistry':3, 'Basics of mechanical engineering':3, 'Engineering practices':1,
      'Communication skills for Engineers/German':2}
Sem3={'Electric circuits':4, 'Circuits & Devices laboratory':2, 'Linear algebra and numerical analysis':4,
      'Electromagnetic theory':3, 'DC machines and transformers':3, 'DC machines and transformers laboratory':1,
      'Building communication skills':2, 'Economics for engineers':3}
Sem4={'Network Theory':4, 'Electronic circuits':3, 'Electronic circuits laboratory':1, 'Probability and statistics':3,
      'Measurements and Instrumentation':3, 'Induction and synchronous machines':3, 
      'Induction and synchronous machines laboratory':2, 'Soft skills development':1}
Sem5={'Digital Electronics':4, 'Control systems':3, 'Electrical Power Generation systems':3, 'Instrumentation and Control Laboratory':1,
      'Digital Electronics laboratory':1, 'Linear Integrated circuits':3,'Power electronics and applications':4,'Business Managerial communications':1}
Sem6={'Embedded Controllers':3, 'Electrical Machine Design':4, 'Power Electronics and Embedded Controllers Laboratory':1, 'Digital Signal Processing':3, 
      'Transmission and Distribution':4, 'Digital signal processing and linear integrated circuits laboratory':1, 'Quantitative and reasoning skills':1}

#input marks
print("Enter the grade point for the following subjects")
print("\nSemester 1")
Sem1_list=[]
for key in Sem1:
    Sem1_list.append(input(key+": "))
print('-'*100)
print("Semester 2")
Sem2_list=[]
for key in Sem2:
    Sem2_list.append(input(key+": "))
print('-'*100)
print("Semester 3")
Sem3_list=[]
for key in Sem3:
    Sem3_list.append(input(key+": "))
print('-'*100)
print("Semester 4")
Sem4_list=[]
for key in Sem4:
    Sem4_list.append(input(key+": "))
print('-'*100)
print("Semester 5")
Sem5_list=[]
for key in Sem5:
    Sem5_list.append(input(key+": "))
print('-'*100)
print("Semester 6")
Sem6_list=[]
for key in Sem6:
    Sem6_list.append(input(key+": "))

# print(Sem1_list,Sem2_list,Sem3_list,Sem4_list)

#Total credits calculation for each semester
totalcredit1=0
for value in Sem1.values():
    totalcredit1=totalcredit1+int(value)
#print(totalcredit1)
totalcredit2=0
for value in Sem2.values():
    totalcredit2=totalcredit2+int(value)
#print(totalcredit2)
totalcredit3=0
for value in Sem3.values():
    totalcredit3=totalcredit3+int(value)
#print(totalcredit3)
totalcredit4=0
for value in Sem4.values():
    totalcredit4=totalcredit4+int(value)
#print(totalcredit4)
totalcredit5=0
for value in Sem5.values():
    totalcredit5=totalcredit5+int(value)
totalcredit6=0
for value in Sem6.values():
    totalcredit6=totalcredit6+int(value)

#Total grade calculation for each semester
S1_totalgrade=0
for grade,value in itertools.zip_longest(Sem1_list,Sem1.values()):
      S1_totalgrade=S1_totalgrade+(int(grade)*int(value))
#print(S1_totalgrade)
S2_totalgrade=0
for grade,value in itertools.zip_longest(Sem2_list,Sem2.values()):
      S2_totalgrade=S2_totalgrade+(int(grade)*int(value))
#print(S2_totalgrade)
S3_totalgrade=0
for grade,value in itertools.zip_longest(Sem3_list,Sem3.values()):
      S3_totalgrade=S3_totalgrade+(int(grade)*int(value))
#print(S3_totalgrade)
S4_totalgrade=0
for grade,value in itertools.zip_longest(Sem4_list,Sem4.values()):
      S4_totalgrade=S4_totalgrade+(int(grade)*int(value))
# print(S4_totalgrade)
S5_totalgrade=0
for grade,value in itertools.zip_longest(Sem5_list,Sem5.values()):
      S5_totalgrade=S5_totalgrade+(int(grade)*int(value))
S6_totalgrade=0
for grade,value in itertools.zip_longest(Sem6_list,Sem6.values()):
      S6_totalgrade=S6_totalgrade+(int(grade)*int(value))
# print(S5_totalgrade)
#print(f"total grade for sem1 {S1_totalgrade}".format(S1_totalgrade))

print('='*50)
#Calculation of GPA for each semester
S1_GPA=S1_totalgrade/totalcredit1
S2_GPA=S2_totalgrade/totalcredit2
S3_GPA=S3_totalgrade/totalcredit3
S4_GPA=S4_totalgrade/totalcredit4
S5_GPA=S5_totalgrade/totalcredit5
S6_GPA=S6_totalgrade/totalcredit6

#Calculation of CGPA
CGPA=(S1_GPA+S2_GPA+S3_GPA+S4_GPA+S5_GPA+S6_GPA)/6

#create a txt file for output
f=open(os.path.join(sys.path[0], "CGPA.txt"), "w")
f.write(f"GPA of 1st Semester: {S1_GPA}\nGPA of 2st Semester: {S2_GPA}\nGPA of 3st Semester: {S3_GPA}\n
      GPA of 4st Semester: {S4_GPA}\nGPA of 5st Semester: {S5_GPA}\nGPA of 6st Semester: {S6_GPA}\n\nCGPA: {CGPA}""".format(S1_GPA,S2_GPA,S3_GPA,S4_GPA,S5_GPA,S6_GPA,CGPA))
f.close()

