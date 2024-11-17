from django.db import models
from municipalities.models import Municipality
from states.models import State


class City(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='cities')
    municipality = models.ForeignKey(
        Municipality,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='cities'
    )

    def __str__(self):
        if self.municipality:
            return f"{self.name}, {self.municipality.name}, {self.state.name}"
        return f"{self.name}, {self.state.name}"
