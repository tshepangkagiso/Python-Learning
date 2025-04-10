# Create a program that simulates a simple database using file I/O. Implement functions to add records, search for 
# records, update records, and delete records. Store the data in a CSV or JSON format.

import os
import Employee as Employees
import Database as Data
import time

# data storage
folder_name = "File Input Output\\exercise 1\\Data"
os.makedirs(folder_name, exist_ok= True)
file_path = os.path.join(folder_name, "JsonDB.json")
db = Data.Database(file_path)

if os.path.exists(file_path) == False:
    db.CreateJson()


def CreateEmployees():
    employee1 = Employees.Employee(1, "John Smith", "HR").MapToDictionary()
    employee2 = Employees.Employee(2, "Mary Johnson", "Finance").MapToDictionary()
    employee3 = Employees.Employee(3, "James Williams", "IT").MapToDictionary()
    employee4 = Employees.Employee(4, "Patricia Brown", "Marketing").MapToDictionary()
    employee5 = Employees.Employee(5, "Michael Davis", "Operations").MapToDictionary()
    employee6 = Employees.Employee(6, "Linda Garcia", "Sales").MapToDictionary()
    employee7 = Employees.Employee(7, "Robert Martinez", "Customer Support").MapToDictionary()
    employee8 = Employees.Employee(8, "Elizabeth Hernandez", "Legal").MapToDictionary()
    employee9 = Employees.Employee(9, "David Lopez", "R&D").MapToDictionary()
    employee10 = Employees.Employee(10, "Sarah Wilson", "Product Management").MapToDictionary()


    # Add all employees to the database
    db.AddRecords(employee1)
    db.AddRecords(employee2)
    db.AddRecords(employee3)
    db.AddRecords(employee4)
    db.AddRecords(employee5)
    db.AddRecords(employee6)
    db.AddRecords(employee7)
    db.AddRecords(employee8)
    db.AddRecords(employee9)
    db.AddRecords(employee10)
def sleep():
  time.sleep(3)  


#CreateEmployees()

employee11 = Employees.Employee(11, "John Wick", "Leyora").MapToDictionary()
sleep()

db.AddRecords(employee11)
sleep()

db.GetAll()
sleep()

db.GetByID(11)
sleep()

db.UpdateRecordByID(11, "Wick", "JW4")
sleep()

db.DeleteRecordByID(11)
sleep()

db.GetByID(11)
sleep()

db.GetAll()
sleep()



