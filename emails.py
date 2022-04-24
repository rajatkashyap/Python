emails='''from rajat.kas@gmail.com
from rajat.kashyap@gmail.com
from parag.kashyap@gmail.com
from charubehl1086@gmail.com
from rajat.kashyap@aig.com
from rajatkashyap@yahoo.com'''

emails_l=emails.split('\n')
#print emails_l
emails_names=[]
email_d=[]
for email in emails_l:
	i=email.index(' ')
	j=email.index('@')
	emails_names.append(email[i+1:j])
	email_d.append(email[j+1:])

print emails_names
print email_d
