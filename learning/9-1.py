class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"restaurant_name:{self.restaurant_name},cuisine_type:{self.cuisine_type}")

    @staticmethod
    def open_restaurant():
        print('The restaurant is open.')


restaurant = Restaurant('A restaurant', 'A cuisine_type')
print(restaurant.restaurant_name, restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
