with open("in.txt") as f:
    content = f.read().strip()
numbers = [int(i) for i in content.split(",")]

def custom_sort(numbers):
    # return numbers sorted in ascending order   
    return None

#  print result
print("sorted: ", custom_sort(numbers))

