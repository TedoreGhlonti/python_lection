class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):

        print(f"Welcome to {self.restaurant_name}!")
        print(f"We serve delicious {self.cuisine_type} cuisine.")

    def open_restaurant(self):

        print(f"The restaurant {self.restaurant_name} is now OPEN!")

restaurant1 = Restaurant("Guria", "Georgian")
restaurant2 = Restaurant("Pizza", "Italianan")
restaurant3 = Restaurant("Sushi", "China")
print(f"Restaurant Name: {restaurant1.restaurant_name}")
print(f"Cuisine Type: {restaurant1.cuisine_type}")
restaurant1.describe_restaurant()
restaurant1.open_restaurant()
print(f"Restaurant Name: {restaurant2.restaurant_name}")
print(f"Cuisine Type: {restaurant2.cuisine_type}")
restaurant2.describe_restaurant()
restaurant2.open_restaurant()
print(f"Restaurant Name: {restaurant3.restaurant_name}")
print(f"Cuisine Type: {restaurant3.cuisine_type}")
restaurant3.describe_restaurant()
restaurant3.open_restaurant()