from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=150)

    def __str__(self):
        return self.name