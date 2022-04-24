daily_balances = [107.92, 108.67, 109.86, 110.15]
def show_balance(daily_balances):
	l=len(daily_balances)
	for day in range(l-3,l-1):
		print daily_balances[day:day+2]
	
show_balance(daily_balances)