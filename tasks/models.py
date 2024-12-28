from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name