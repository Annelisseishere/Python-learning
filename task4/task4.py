with open("in.txt") as f:
    content = f.read().strip()
numbers = [int(i) for i in content.split(",")]

def custom_sort(numbers):
    # return numbers sorted in ascending order   
    for i, num_i in enumerate(numbers[:-1]):
        for j, num_j in enumerate(numbers[:-1]):
            if numbers[j] > numbers[j+1]:
                temp = numbers[j+1]
                numbers[j+1] = numbers[j]
                numbers[j] = temp

    return numbers

#  print result
print("sorted: ", custom_sort(numbers))



###### while approach ######
#def sorting(numbers):
    #i = 0
    #j = 0
    #while i < len(numbers)-1:
        #while j < len(numbers)-1:
            #if numbers[j] > numbers[j+1]:
                #temp = numbers[j+1]
                #numbers[j+1] = numbers[j]
                #numbers[j] = temp  
            #j = j + 1
        #i = i + 1
        #j = 0
        
    #return numbers

#print("sorted: ", sorting(numbers))