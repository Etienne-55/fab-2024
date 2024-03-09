from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    abilities = models.CharField(max_length=255, default='None')
    stats = models.CharField(max_length=255, default='None')

    def __str__(self):
        return self.name
