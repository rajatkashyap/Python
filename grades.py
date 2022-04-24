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
grade_dicts={}
for i in grades:
    if i[0]!='Student':
    	marks={}
    	marks['Exam 1']=int(i[1])
    	marks['Exam 2']=int(i[2])
    	marks['Exam 3']=int(i[3])
    	grade_dicts[i[0]]=marks

'''for i in grades:
    if i[0]!='Student':
    	grade_dicts[i[0]]['Exam 1']=i[1]
    	grade_dicts[i[0]]['Exam 2']=i[2]
    	grade_dicts[i[0]]['Exam 3']=i[3]	

print grade_dicts'''
print marks 
print grade_dicts
print grade_dicts['Ursula']['Exam 1']