with open("in.txt") as f:
    content = f.read().strip()
numbers = [int(i) for i in content.split(",")]

def custom_sort(numbers):
    for i in range(0, len(numbers)): # TODO: start from 1
		# Assumption: numbers[0:i] are sorted (mathematical interval is [0,i) i.e. without i)
		# insert numbers[i] at index j where j in [0,i]
		# idea:
		# * start at j = i
		# * iterate in descending order until current number is no longer greater than numbers[i]
		# * while iterating move current number one index higher
		# * after while loop insert numbers[i] at index of last greater number
        j = i 
        for j in range(0, len(numbers)):
            if numbers[j-1] > numbers[j] and j > 0:
                temp = numbers[j-1]
                numbers[j-1] = numbers[j]
                numbers[j] = temp
                j = j-1
    
    return numbers

print("sorted: ", custom_sort(numbers))
