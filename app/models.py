from django.db import models

# Create your models here.

class Element(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False)
    date_element = models.DateField()
