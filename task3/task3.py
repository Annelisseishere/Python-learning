with open("in.txt") as f:
    content = f.read().strip()
numbers = [int(i) for i in content.split(",")]

def two_sum(numbers, target):
    diff1 = abs(numbers[0] + numbers[1] - target)
    result = (numbers[0], numbers[1], diff1)

    for i,num_i in enumerate(numbers):
        for j,num_j in enumerate(numbers):
            diff2 = abs(numbers[i] + numbers[j] - target)
            if diff2 <= diff1:
                if numbers[i] != numbers[j]:
                    diff1 = diff2
                    result = (numbers[i], numbers[j], diff1)
  


    # TODO: Return 2 numbers from the input *numbers* array which sum up to *target*
    
        
    return result 
#  print result
# should print 24 and 16
print("TWO SUM: ", two_sum(numbers, 40))

