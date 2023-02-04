with open("in.txt") as f:
    content = f.read().strip()
numbers = [int(i) for i in content.split(",")]

def custom_sort(numbers):
    i = 0
    j = 0
    while i < len(numbers)-1:
        while j < len(numbers)-1:
            if numbers[j] > numbers[j+1]:
                temp = numbers[j+1]
                numbers[j+1] = numbers[j]
                numbers[j] = temp  
            j = j + 1
        i = i + 1
        j = 0
        
    return numbers

        

print("sorted: ", custom_sort(numbers))