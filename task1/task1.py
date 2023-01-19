with open("in.txt") as f:
    content = f.read().strip()
numbers = [int(i) for i in content.split(",")]
max_number = max(numbers)
# TODO: Find max element in numbers array

print(max_number)
