from datetime import datetime

class Person:
    def __init__(self, name, country, birthdate):
        self.name = name
        self.country = country
        self.birthdate = birthdate

    def calculate_age(self):
        today = datetime.now()
        birthdate = datetime.strptime(self.birthdate, "%Y-%m-%d")
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return age

person = Person("John Doe", "USA", "1990-05-15")
age = person.calculate_age()
print(f"{person.name} is {age} years old.")
print(f"{person.name} is from {person.country}.")
