from django.db import models
from django.core.exceptions import ValidationError


class Musician(models.Model):
    MINIMUM_AGE = 18

    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    instrument = models.CharField(max_length=63)
    age = models.IntegerField()
    date_of_applying = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def is_adult(self):
        return self.age >= 21

    def clean(self):
        if self.age is not None and self.age < self.MINIMUM_AGE:
            raise ValidationError(
                {"age": f"Age must be at least {self.MINIMUM_AGE}."}
            )
