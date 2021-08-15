from django.db import models
from django.db.models.fields import CharField, TextField

class Categories(models.Model):
    name = CharField(max_length=100)
    description = TextField(max_length=1000,blank=True)
    description_min = TextField(max_length=1000,blank=True)
    image = models.ImageField(upload_to="Images0",blank=True,default=0)

    class Meta:
        db_table = "Types_of_idols"\
    
    def __str__(self):
        return self.name

class Idol(models.Model):
    model_no = models.CharField(max_length=20)
    model_name = models.CharField(max_length=20,blank=True)
    height = models.CharField(max_length=20)
    featured = models.CharField(max_length=20,blank=True)
    price = models.CharField(max_length=100,blank=True)
    image1 = models.ImageField(upload_to="Images1")
    image2 = models.ImageField(upload_to="Images2",blank=True)
    image3 = models.ImageField(upload_to="Images3",blank=True)
    category = models.ForeignKey(Categories,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.model_no

    class Meta:
        db_table="Idols"

class ContactMe(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    subject = models.CharField(max_length=500)
    message = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.email

    class Meta:
        db_table="ContactMe"