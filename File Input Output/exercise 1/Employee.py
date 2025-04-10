class Employee:
    def __init__(self, ID,Name,Department):
        self.ID = ID
        self.Name = Name
        self.Department = Department

    def MapToDictionary(self):
        return {"ID": self.ID, "Name": self.Name, "Department": self.Department}
    
        