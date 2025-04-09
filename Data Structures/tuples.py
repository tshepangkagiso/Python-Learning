#Write a function that takes a list of numbers and returns a tuple containing the minimum, maximum, and average values.
list_of_numbers = [1,2,3,4,5,6,7,8,9,10]

def returnTuple():
    list_of_numbers.sort()
    min = list_of_numbers[0]
    max = list_of_numbers[len(list_of_numbers) - 1]
    total = 0
    for num in list_of_numbers:
        total += num
    avg = total/len(list_of_numbers)
    return (min,max,avg)

(min,max,avg) = returnTuple()

print(f'min: {min}')
print(f'max: {max}')
print(f'avg: {avg}')