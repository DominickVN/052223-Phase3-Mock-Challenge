class Restaurant:
    def __init__(self, name):
        self._name = None
        self.name = name
        self._reviews = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if len(value) < 1:
            raise ValueError("Name must be 1 or more characters")
        if self._name is not None:
            raise ValueError("Name cannot be changed after the resturant is created")
        self._name = value

    def add_review(self, review):
        self._reviews.append(review)

    def average_star_rating(self):
        if not self._reviews:
            return 0.0

        total_rating = sum(review.rating for review in self._reviews)
        num_reviews = len(self._reviews)
        return total_rating / num_reviews

    @classmethod
    def get_all_restaurants(cls):
        pass