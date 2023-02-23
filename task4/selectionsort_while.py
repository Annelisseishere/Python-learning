with open("in.txt") as f:
    content = f.read().strip()
numbers = [int(i) for i in content.split(",")]

def custom_sort(numbers):
    i = 0
    while i < len(numbers):
        min_value = numbers[i]
        j = i + 1
        index = i
        while j < len(numbers):
            if numbers[j] < min_value:
                min_value = numbers[j]
                index = j
            j = j+1
        temp = numbers[i]
        numbers[i] = min_value
        numbers[index] = temp
        i = i + 1 
     

    return numbers

print("sorted: ", custom_sort(numbers))
                
                
            