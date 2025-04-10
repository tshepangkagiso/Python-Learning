import json
import os

class Database:
    def __init__(self, path):
        self.path = path
    
    # create db file
    def CreateJson(self):
        open(self.path, 'w').close()
        
    # function to add records
    def AddRecords(self, data):
        try:
            employees = []
            if os.path.getsize(self.path) > 0:
                with open(self.path, "r") as file:
                    employees = list(json.load(file))

            employees.append(data)
            
            with open(self.path, "w") as file:
                json.dump(employees, file, indent=4)

            print(f"Successfully added record: {data}")
        except Exception as e:
            print(f"Failed to add record: {e}")

    # function to search for records
    def GetAll(self):
        try:
            employees = []
            if os.path.getsize(self.path) > 0 and os.path.exists(self.path):
                with open(self.path, "r") as file:
                    employees = list(json.load(file))
            
            if len(employees) > 0:
                for emp in employees:
                    print(emp)
                print("Done getting all records")
            else:
                print("No records found")
        except Exception as e:
            print(f"Failed to get all records: {e}")


    def GetByID(self,ID):
        try:
            employees = []
            if os.path.getsize(self.path) > 0:
                with open(self.path, "r") as file:
                    employees = list(json.load(file))
            if ID > len(employees) or ID <= 0:
                print("Employee not found.")
            else:
                employee = employees[ID -1]
                print(employee)
        except Exception as e:
            print(f"Failed to get record by id: {e}")

    # function to update records
    def UpdateRecordByID(self,ID,Name,Department):
        try:
            employees = []
            if os.path.getsize(self.path) > 0:
                with open(self.path, "r") as file:
                    employees = list(json.load(file))

            if ID <= 0 or ID > len(employees):
                print("Employee not found.")
            else:
                employee = dict(employees[ID - 1])

                if Name and Name != "":
                    employee["Name"] = Name

                if Department and Department != "":
                    employee["Department"] = Department

                # Replace the old employee with the updated one
                employees[ID - 1] = employee

                # Print the updated employee info
                print(f"Updated employee: {employee}")


                with open(self.path, "w") as file:
                    json.dump(employees, file, indent=4)

        except Exception as e:
            print(f"Failed to update record: {e}")     


    # function to delete records
    def DeleteRecordByID(self,ID):
        try:
            employees = []
            if os.path.getsize(self.path) > 0:
                with open(self.path, "r") as file:
                    employees = list(json.load(file))

            if ID > len(employees) or ID <= 0:
                print("Employee not found.")
            else:
                employee = employees.pop(ID - 1)
                print(f"Sucessfully deleted employee: {employee}")

                with open(self.path, "w") as file:
                    json.dump(employees, file, indent=4)

        except Exception as e:
            print(f"Failed to delete record: {e}")
