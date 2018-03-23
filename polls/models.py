from django.db import models




# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=200, default="Name")
    password = models.CharField(max_length=200, default="Password")

    def __str__(self):
        return self.username


class Picture(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    label = models.CharField(max_length=200, default="Label")
    picture = models.ImageField(upload_to='media/', default='no_image.jpg')

