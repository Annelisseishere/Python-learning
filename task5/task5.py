with open("in.txt") as f:
    content = f.read().strip()
numbers = [int(i) for i in content.split(",")]

def remove_duplicates(numbers):
	# given numbers sorted in ascending order, remove all duplicates in-place i.e. you are allowed to only modify the array not create new one
    i = 0
    for j in range(0, len(numbers)-1):
		# This condition is good
        if numbers[i] == numbers[i+1]:
			# don't remove and insert here but shift numbers[i+2] to numbers[i+1]
            for o in range(i+1, len(numbers)-1):
                numbers[o] = None
                numbers[o], numbers[o+1] = numbers[o+1], numbers[o]
        else:
            i = i+1

    return numbers
#  print result
print("removed: ", remove_duplicates(sorted(numbers)))

