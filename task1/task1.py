with open("in.txt") as f:
    content = f.read().strip()
numbers = [int(i) for i in content.split(",")]

# TODO: Find max element in numbers array

max_number = numbers[0]
min_number = max_number

i=1
while i < len(numbers):
    # find min value
    if min_number > numbers[i]:
        min_number = numbers[i]
    # find max value
    if max_number < numbers[i]:
        max_number = numbers[i]
    # increment, could be i += 1
    i = i + 1

# print min
print("MIN VALUE: ", min_number)

# print max
print("MAX VALUE: ", max_number)


    


