def numbers(n):
	

	nums = [45, 55, 60, 37, 100, 105, 220]

	for value in nums:
		if value % n == 0:
			print(value)
		else:
			print('Ne delitsa, vvedite drygoe chislo')
