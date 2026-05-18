class Restourant:

    def __init__(self, restourant_name, cuisine_type):
        self.restourant_name = restourant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restourant(self):

        return f"Welcome to {self.restourant_name}, We serve delicious {self.cuisine_type} cuisine.!"
        
    def open_restaurant(self):
        return f"The restaurant {self.restourant_name} is now OPEN!"
    
    def set_number_served(self, number):
        self.number_served = number
        return f"Number of served customers set to {self.number_served}."

    def increment_number_served(self, additional_customers):
        self.number_served += additional_customers
        return f"Served {additional_customers} more customers. Total now: {self.number_served}."
    
class IceCreamStand(Restourant):

    def __init__(self, restaurant_name, cuisine_type="Ice Cream"):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def display_flavors(self):
        print(f"Available flavors at {self.restourant_name}:")
        for flavor in self.flavors:
            print(f"- {flavor}")

my_icecream = IceCreamStand("Gelato")
my_icecream.flavors = ["Vanilla", "Chocolate", "Strawberry", "Pistachio"]
print(my_icecream.display_flavors())
print(my_icecream.describe_restourant())
my_restourant = Restourant("Tbilisi", "Georgian")
print(my_restourant.describe_restourant())
print(my_restourant.open_restaurant())