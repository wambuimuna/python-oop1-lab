#!/usr/bin/env python3
class Coffee:
    def __init__(self, size, price):
        self._size = None
        self.price = price
        self.size = size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        valid = ("Small", "Medium", "Large")
        if value in valid:
            self._size = value
        else:
            print("size must be Small, Medium, or Large")

    def tip(self):
        # use the curly apostrophe to match the tests
        print("This coffee is great, here’s a tip!")
        try:
            self.price = float(self.price) + 1
        except Exception:
            self.price = self.price