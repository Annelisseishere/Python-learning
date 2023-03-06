
def increment(number1, number2):
	# Given 2 numbers represented as array of digits (same as in the previous task) perform addition between the two and return resulting array.
	if len(number1) < len(number2):
		number1, number2 = number2, number1
	m = len(number1)
	n = len(number2)
	i = m-1
	j = n-1
	oflow = 0
	while j >= 0:
		temp = number1[i] + number2[j] + oflow
		if temp < 10:
			number1[i] = temp
			oflow = 0
		else:
			number1[i] = temp - 10
			oflow = 1
	#increment
		i = i-1
		j = j-1

	while i >= 0:
		temp = number1[i] + oflow
		if temp < 10:
			number1[i] = temp
			oflow = 0
		else:
			number1[i] = temp - 10
			oflow = 1
	#increment
		i = i-1
	
	#increase digits
	if oflow == 1:
		number1.insert(0,1)	

	return number1

#  print the result. [1, 1, 9, 8] is expected.
print("added: ", increment([1, 0, 9, 9], [9, 9]))
