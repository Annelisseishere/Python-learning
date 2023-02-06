with open("in.txt") as f:
    content = f.read().strip()
numbers = [int(i) for i in content.split(",")]

def remove_duplicates(numbers):
	# given numbers sorted in ascending order, remove all duplicates in-place i.e. you are allowed to only modify the array not create new one
    return numbers
 
#  print result
print("removed: ", remove_duplicates(sorted(numbers)))

