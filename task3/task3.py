with open("in.txt") as f:
    content = f.read().strip()
numbers = [int(i) for i in content.split(",")]

def two_sum(numbers, target):
    # TODO: Return 2 numbers from the input *numbers* array which sum up to *target*

# print result
# should print 24 and 16
print("TWO SUM: ", two_sum(numbers, 40))

