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
grades_by_assignment_test={}
l1=[]
l2=[]
l3=[]
for i in grades:
    if i[0]!='Student':
    	l1.append(i[1])
        l2.append(i[2])
        l3.append(i[3])
grades_by_assignment_test['Exam 1']=l1
grades_by_assignment_test['Exam 2']=l2
grades_by_assignment_test['Exam 3']=l3       
print grades_by_assignment_test
