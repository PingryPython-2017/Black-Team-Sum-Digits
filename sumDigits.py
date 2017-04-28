# sum_digits

def sum_digits(num):
	'''Takes in a nonnegative integer, and tells the sum of each of the digits.'''
	if num == 0:
		return 0
	else:
		return num % 10 + sum_digits(num // 10)
