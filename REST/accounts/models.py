from django.contrib.auth.models import User
from django.db import models
# Create your models here.


class Profile(models.Model):
    full_name = models.CharField(max_length=78)
    image = models.ImageField()
    age = models.PositiveIntegerField()
    date_join = models.DateField()
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    wallet = models.PositiveIntegerField(default=0)
    address = models.CharField(max_length=90)
    def __str__(self):
        return self.full_name