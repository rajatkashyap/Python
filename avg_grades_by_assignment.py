grades = [
    # First line is descriptive header. Subsequent lines hold data
    ['Student', 'Exam 1', 'Exam 2', 'Exam 3'],
    ['Thorny', '100', '90', '80'],
    ['Mac', '88', '99', '111'],
    ['Farva', '45', '56', '67'],
    ['Rabbit', '59', '61', '67'],
    ['Ursula', '73', '79', '83'],
    ['Foster', '89', '97', '101']
]
import numpy as n
avg_grades_by_assignment={}
l1=[]
l2=[]
l3=[]
for i in grades:
    if i[0]!='Student':
    	l1.append(int(i[1]))
        l2.append(int(i[2]))
        l3.append(int(i[3]))
avg_grades_by_assignment['Exam 1']=n.mean(l1)
avg_grades_by_assignment['Exam 2']=n.mean(l2)
avg_grades_by_assignment['Exam 3']=n.mean(l3)      
print avg_grades_by_assignment