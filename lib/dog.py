#!/usr/bin/env python3

class Dog:
    APPROVED_BREEDS = [
        "Mastiff",
        "Chihuahua",
        "Corgi",
        "Shar Pei",
        "Beagle",
        "French Bulldog",
        "Pug",
        "Pointer"
    ]

    def __init__(self, name: str = "Dog", breed: str = "Mastiff"):
        self._name = None
        self._breed = None
        self.name = name  # Calls the name setter
        self.breed = breed  # Calls the breed setter

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
        else:
            print("Name must be string between 1 and 25 characters.")

    @property
    def breed(self) -> str:
        return self._breed

    @breed.setter
    def breed(self, value: str):
        if value in self.APPROVED_BREEDS:
            self._breed = value
        else:
            print("Breed must be in list of approved breeds.")

