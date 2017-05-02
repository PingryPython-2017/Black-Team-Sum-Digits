# sum_digits

def sum_digits(num):
	'''Takes in a non-negative integer, and tells the sum of each of the digits.'''
	if num == 0: # Making a terminating case, with an if statement
		return 0 # Terminating Case always returns 0
	else:
		return num % 10 + sum_digits(num // 10) # Recursive Case

