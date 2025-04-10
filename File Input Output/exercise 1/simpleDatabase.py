# Create a program that simulates a simple database using file I/O. Implement functions to add records, search for 
# records, update records, and delete records. Store the data in a CSV or JSON format.

import os
import Employee
import Database

# data storage
folder_name = "File Input Output\exercise 1\Data"
os.makedirs(folder_name, exist_ok= True)
file_path = os.path.join(folder_name, "JsonDB.json")

employee1 = Employee(1,"John", "HR")

db = Database(file_path)
db.AddRecords(employee1)



