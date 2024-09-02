#!/usr/bin/env python3

class Person:
    APPROVED_JOBS = [
        "Admin",
        "Customer Service",
        "Human Resources",
        "ITC",
        "Production",
        "Legal",
        "Finance",
        "Sales",
        "General Management",
        "Research & Development",
        "Marketing",
        "Purchasing"
    ]

    def __init__(self, name: str = "John Doe", job: str = "Admin"):
        self._name = None
        self._job = None
        self.name = name  # Calls the name setter
        self.job = job  # Calls the job setter

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value.title()
        else:
            print("Name must be string between 1 and 25 characters.")

    @property
    def job(self) -> str:
        return self._job

    @job.setter
    def job(self, value: str):
        if value in self.APPROVED_JOBS:
            self._job = value
        else:
            print("Job must be in list of approved jobs.")

