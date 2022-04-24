states={'California':'CA','Texas':'TX','Arizona':'AZ'}
city={'TX':'Houston'}
city['AZ']='Phoenix'
city['CA']='Los Angles'

print city[states['Texas']]

print city

print city.items()

for state,abbr	 in states.items():
	print "%s state is abbreviated %s and has city %s" %(state,abbr,city[abbr])

print states.items()