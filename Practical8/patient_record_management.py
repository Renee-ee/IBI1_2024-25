class patient:
    def __init__ (self, name, age, date, medical):
        self.name = name
        self.age = age
        self.date = date
        self.medical = medical
    def pri(self):
        print ("Individual's name:", self.name, '/n',"Age:", self.age, "Date of latest admission:", self.date, "Medical history:", self.medical)

#name = 1212
#age = 20
#date = "2020.1.2"
#medical = "cold"
patient1= patient("Resoo", 20, "2020.1.2", "cold")

patient1.pri()