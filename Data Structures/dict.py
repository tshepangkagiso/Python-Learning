#Create a program that simulates a simple phonebook using a dictionary. Allow users to add, delete, and look up entries
phonebook_dictionary = {}

def addPhonebook():
    name = input("enter new name: ")
    number = input('enter new number: ')
    phonebook_dictionary[name] = number

    print(f"new user: {phonebook_dictionary[name]}")


def deletePhonebook():
    name = input("enter name to delete: ")
    phonebook_dictionary.pop(name)

def findPhonebook():
    for name, number in phonebook_dictionary.items():
        print(f"{name}: {number}")


addPhonebook()
findPhonebook()
deletePhonebook()