from django.db import models
from states.models import State


class Municipality(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='municipalities')

    def __str__(self):
        return f"{self.name}, {self.state.name}"
