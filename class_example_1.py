import datetime

class User:
    """Some text on the class which is used to create objects.
    More description 
    Blah 
    SHows how classes can be assigned fields, methods and how we can create an object instance"""

    def __init__(self,full_name, birthday):
        self.name = full_name
        self.dob = birthday   ### YYYYMMDD

        name_pieces = full_name.split(" ")
        self.first = name_pieces[0]
        self.last = name_pieces[-1]

    ## age is a method / function
    def age(self):
        """Return age """
        today = datetime.date.today()
        age_year=int(self.dob[0:4])
        age_month=int(self.dob[4:6])
        age_day=int(self.dob[6:8])
        dob = datetime.date(age_year, age_month, age_day)
        age_in_days = (today - dob).days
        age_in_years= age_in_days / 365
        return int(age_in_years)

        



user1= User("Bob Dylan","19780101 ")
print(user1.name)
print(user1.dob)
print(user1.first) 
print(user1.last)
help(User)

print(user1.age())
