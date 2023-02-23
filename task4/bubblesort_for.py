with open("in.txt") as f:
    content = f.read().strip()
numbers = [int(i) for i in content.split(",")]

def custom_sort(numbers):
    for i,num_i in enumerate(numbers[:-1]):
        for j,num_j in enumerate(numbers[:-1]):
            if numbers[j] > numbers[j+1]:
                temp = numbers[j+1]
                numbers[j+1] = numbers[j]
                numbers[j] = temp  
                
    return numbers

        

print("sorted: ", custom_sort(numbers))