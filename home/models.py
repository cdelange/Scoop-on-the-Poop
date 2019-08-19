from django.db import models
from datetime import datetime


class Dog(models.Model):
    name = models.CharField(max_length=6)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=6)

    def __str__(self):
        return self.name


class BathroomBreak(models.Model):
    dog = models.ForeignKey(Dog, related_name='bathroom_breaks', on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=datetime.now)
    type_of_bathroom = models.CharField(max_length=6)
    person = models.ForeignKey(Person, related_name='persons', default="", on_delete=models.CASCADE)

    def __str__(self):
        return self.type_of_bathroom
