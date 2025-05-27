# Define a class to manage patient records
class patient:
    def __init__ (self, name, age, date, history):
        # Assign input values to object attributes
        self.name = name
        self.age = age
        self.date = date
        self.history = history
    def pri(self):
        # A fuction displays formatted patient information
        print ("Patient name:", self.name,'|', "Age:", self.age,'|', "Date of latest admission:", self.date,'|', "Medical history:", self.history)

#name = Resoo
#age = 20
#date = "2020.1.2"
#history = "cold"

patient1= patient("Resoo", 20, "2020.1.2", "cold")
patient1.pri()