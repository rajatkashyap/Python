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
avg_grades_by_student={}
'''for i in grades:
    if i[0]!='Student':
    	avg_grades_by_student[i[0]]=sum(list(map(int,i[1:])))/3

'''		
for i in grades:
	if i[0]!='Student':
		avg_grades_by_student[i[0]]=(int(i[1])+int(i[2])+int(i[3]))/3.0
		

'''for i in grades:
    if i[0]!='Student':
    	grade_dicts[i[0]]['Exam 1']=i[1]
    	grade_dicts[i[0]]['Exam 2']=i[2]
    	grade_dicts[i[0]]['Exam 3']=i[3]	

print grade_dicts'''
print avg_grades_by_student 
