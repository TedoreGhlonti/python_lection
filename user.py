class User:

    def __init__(self, first_name, last_name, age, city):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city

    def describe_user(self):

        return f"User name is {self.first_name} {self.last_name}, user is {self.age} years old and user lives in {self.city}"

    def greet_user(self):

        return f"Hello {self.first_name} {self.last_name}!" 
    
user = User("Tedore", "Ghlonti", 43, "Ozurgeti")
print(user.describe_user())
print(user.greet_user())
user1 = User("Saba", "Vadachkoria", 23, "Tbilisi")
print(user1.describe_user())
print(user1.greet_user())


        
        