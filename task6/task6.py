
def increment(number):
	# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.
	# The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
	# Increment the large integer by one and return the resulting array of digits.                
	n = len(number)
	i = n-1
	temp = 1
	while i >= 0:
		if number[i] == 9:
			number[i] = 0
		else:
			number[i] +=temp
			temp = 0
			break

		i = i-1
	
	#increase digits
	if temp == 1:
		number.insert(0,1)		
		

	return number

#  print the result. [1, 1, 0, 0] is expected.
print("incremented: ", increment([1, 0, 9, 9]))
