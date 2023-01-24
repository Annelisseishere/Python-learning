with open("in.txt") as f:
    content = f.read().strip()
numbers = [int(i) for i in content.split(",")]

def closest(numbers, target):
    result = numbers[0]
    i=1
    while i < len(numbers):
        if target == result:
            result = target
            break
        else:
            min_value = abs(target - result)
            #print(target, numbers[i])
            if target == numbers[i]:
                result = numbers[i]
                break
            else:
                temp = abs(target - numbers[i])
                #print(numbers[i], temp, min_value)
                if temp < min_value:
                    min_value = temp
                    result = numbers[i]

        i = i + 1


    # TODO: find closest number to target (can be equal to target)


    return result

# print 
print("CLOSEST VALUE: ", closest(numbers, 25))



    


