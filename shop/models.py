from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    bio = models.TextField()


class Media(models.Model):
    image = models.ImageField(upload_to='products')

class Meta_Data(models.Model):
    name = models.CharField(max_length=20)

class Varient(models.Model):
    name = models.CharField(max_length=20)

class Collection(models.Model):
    name = models.CharField(max_length=20)

class Tags(models.Model):
    name = models.CharField(max_length=20)


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    price = models.IntegerField()
    compare_at_price = models.IntegerField()
    quantity = models.IntegerField()
    varient = models.ForeignKey(Varient, on_delete=models.CASCADE)
    meta_data = models.ForeignKey(Meta_Data, on_delete=models.CASCADE)
    category = models.CharField(max_length=50)
    pro_type = models.CharField(max_length=50)
    vender = models.CharField(max_length=50)
    collections = models.ForeignKey(Collection, on_delete=models.CASCADE)
    tags = models.ForeignKey(Tags, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    