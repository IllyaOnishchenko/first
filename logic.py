def numbers(n):
	

	nums = [45, 55, 60, 37, 100, 105, 220]

	for value in nums:
		if value % n == 0:
			print(value)
	for value2 in nums:
		if value2 % n != 0:
			print(value2, '- Число не делиться')
