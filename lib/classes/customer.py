class Customer:
    def __init__(self, first_name, last_name):
        self._first_name = None
        self._last_name = None
        self.first_name = first_name
        self.last_name = last_name
        self._reviews = []

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise ValueError('First name must be a string')
        if not (1 <= len(value) <= 25):
            raise ValueError("First name must be between 1 and 25 character")
        self._first_name = value
    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if not isinstance(value, str):
            raise ValueError("Last name must be a string")
        if not (1 <= len(value) <= 25):
            raise ValueError("Last name must be between 1 and 25 characters")
        self._last_name = value

    def add_review(self, review):
        self._reviews.append(review)

    def restaurants(self):
        restaurant_set = set()
        for review in self._reviews:
            restaurant_set.add(review.restaurant)
        return list(restaurant_set)

    def reviews(self):
        return self._reviews
    def num_reviews(self):
        return len(self._reviews)
