from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=3, unique=True)
    uses_municipalities = models.BooleanField(default=False)

    def __str__(self):
        return self.name
