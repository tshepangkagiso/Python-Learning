#Write a program that creates a list of numbers and performs various operations (append, insert, remove, pop, index, count, sort, reverse).

list_of_numbers = [1,2,3,4,5,6,7,8,9,10]

#appending list
def appendList():
    value = int(input('Enter new value: '))
    list_of_numbers.append(value)
    print(list_of_numbers)

#insert into list
def insertList():
    value = int(input('Enter new value: '))
    index = len(list_of_numbers)
    list_of_numbers.insert(index,value)
    print(list_of_numbers)

#remove item in list
def removeList():
    item = int(input('Enter item: '))
    list_of_numbers.remove(item)
    print(list_of_numbers)

#pop item in list
def popList():
    list_of_numbers.pop()
    print(list_of_numbers)

#find index of number in list
def indexList():
    value = int(input('Enter Index: '))
    index = list_of_numbers.index(value)
    print(f'Value {value } : Index {index}')

#find count of list
def countList():
    count = len(list_of_numbers)
    print(f'count of list: {count}')

#sort the list
def sortList():
    list_of_numbers.sort()
    print(list_of_numbers)

#reverse the list
def reverseList():
    list_of_numbers.reverse() # reverse list
    print(list_of_numbers)


appendList()
print('\n')

popList()
print('\n')

insertList()
print('\n')

removeList()
print('\n')

indexList()
print('\n')

countList()
print('\n')

sortList()
print('\n')

reverseList()
print('\n')