import datetime
class user:
    """Hello, now you will only provide your username and birthday"""
    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday

        #extract the first and last name 
        name_pieces = full_name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]

    def age(self):
        """Returns the age of the user in years"""
        today = datetime.date(2022,6,20)
        dd = int(self.birthday[6:8])
        mm = int(self.birthday[4:6])
        yy = int(self.birthday[0:4])
        dob = datetime.date(yy, mm, dd)
        age_in_days = (today-dob).days
        age_in_years = age_in_days / 365
        return int(age_in_years)
user = user("Kenneth Komu", "20020621")
print(user.age())