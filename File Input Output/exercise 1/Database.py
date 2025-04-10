import json

class Database:
    def __init__(self, path):
        self.path = path
    
    
    # function to add records
    @staticmethod
    def AddRecords(self, data):
        with open(self.path, "a") as file:
            json.dump(data,file,indent=4)

    # function to search for records
    # function to update records
    # function to delete records