from django.db import models
from django.db.models.fields import CharField

class Categories(models.Model):
    name = CharField(max_length=100)