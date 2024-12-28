from django.db import models




class Item(models.Model):
    name = models.CharField(default='', max_length=200, null=False, blank=False)
    password = models.CharField(default='', max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name
