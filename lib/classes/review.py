from classes.customer import Customer
from classes.restaurant import Restaurant

class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self._customer = None
        self._restaurant = None
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        self.__class__.all_reviews.append(self)

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        if not isinstance(value, Customer):
            raise ValueError("Customer must be an instance of Customer class")
        self._customer = value
    @property
    def restaurant(self):
        return self._restaurant

    @restaurant.setter
    def restaurant(self, value):
        if not isinstance(value, Restaurant):
            raise ValueError("Restaurant must be an instance of Restaurant class")
        self._restaurant = value

    @property
    def rating(self):
        return self._rating
    @rating.setter
    def rating(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Rating must be a number")
        if not (1 <= value <= 5):
            raise ValueError("Rating must be between 1 and 5, inclusive")
        self._rating = value