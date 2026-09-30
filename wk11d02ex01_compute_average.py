def computeAverage(numbers):
    total = 0
    count = 0
    for i in range(0, 3 + 1, 1):
        num = numbers[i]
        if num == 0:
        else:
            total = total + num
            count = count + 1
    average = total / count
    
    return average

# Main
numbers = [0] * (4)

numbers[0] = 22
numbers[1] = 9
numbers[2] = 0
numbers[3] = 17
average = computeAverage(numbers)
print(average)
