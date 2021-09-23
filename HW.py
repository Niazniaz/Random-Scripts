class society:
    def __init__(self):
        self.society_name="Surya Apartments"
        self.house_no=20
        self.no_of_memebers=3
        self.flat="A Type"
        self.income=25000
    def inputdata(self):
        self.society=raw_input("Enter Society name")
        self.house_no=input("Enter house number")
        self.members=input("Enter no of memebers")
        self.income=input("Enter income")
        self.allocate_flat()
    def allocate_flat(self):
        if self.income>=25000:
            self.flat="A Type"
        elif self.income>=20000:
            self.flat="B Type"
        elif self.income>=15000:
            self.flat="c Type"
        else:
            print "You are too poor."
    def showdata(self):
        print self.society_name,"is the society name"
        print self.house_no,"is the house number"
        print self.no_of_memebers,"is the number of members"
        print self.flat,"is the flat type"
        print self.income,"is the income"

a=society()
a.inputdata()
a.showdata()
