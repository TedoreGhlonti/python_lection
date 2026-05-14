class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):

        print(f"Welcome to {self.restaurant_name}!")
        print(f"We serve delicious {self.cuisine_type} cuisine.")

    def open_restaurant(self):

        print(f"The restaurant {self.restaurant_name} is now OPEN!")

restaurant = Restaurant("Guria", "Georgian")
print(f"Restaurant Name: {restaurant.restaurant_name}")
print(f"Cuisine Type: {restaurant.cuisine_type}")
restaurant.describe_restaurant()
restaurant.open_restaurant()