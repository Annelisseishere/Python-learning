with open("in.txt") as f:
    content = f.read().strip()
numbers = [int(i) for i in content.split(",")]

def remove_duplicates(numbers):
	# given numbers sorted in ascending order, remove all duplicates in-place i.e. you are allowed to only modify the array not create new one
    i = 0
    for j in range(0, len(numbers)-1):
        if numbers[i] == numbers[i+1]:
            numbers.remove(numbers[i])
            numbers.insert(len(numbers), None)
        else:
            i = i+1
        
            
                

    return numbers
#  print result
print("removed: ", remove_duplicates(sorted(numbers)))

