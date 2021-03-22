from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=90)
    description = models.TextField()
    year = models.DateField()
    abbr = models.CharField(max_length=20,unique=True)
    book_file = models.FileField(blank=True)
    author = models.ForeignKey('Author',on_delete=models.SET_NULL,null=True,related_name='books')
    price = models.PositiveIntegerField(default=0)
    sale = models.BooleanField(default=False)
    sale_amount = models.PositiveIntegerField()



    def __str__(self):
        return self.title



class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    date_birth = models.DateField()
    date_death = models.DateField(blank=True)
    country = models.CharField(max_length=30)

    def __str__(self):
        return self.name




class Order(models.Model):
    statuses = (
        ('pending','pending'),
        ('finished','finished'),
    )
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    book = models.ForeignKey('Book',on_delete=models.SET_NULL,null=True,)
    address = models.CharField(max_length=900,null=True,blank=True)
    quantity = models.PositiveIntegerField()
    data = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=statuses,max_length=20,default='pending')
    total_sum = models.PositiveIntegerField(default=0)
    payment_type = models.CharField(choices=(
        ('card', 'card'),
        ('cash', 'cash'),
    ), max_length=90, default='cash')
    promocode = models.CharField(max_length=5,null=True,blank=True)



    def __str__(self):
        try:
            return self.book.title
        except AttributeError:
            return {"книга не найдена "}


    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'



class Branch(models.Model):
    name = models.CharField(max_length=70)


class Contact(models.Model):
    type = (
        ('email','email'),
        ('phone','phone'),
        ('address','address'),
    )
    types = models.CharField(choices=type,max_length=20,)
    info = models.CharField(max_length=155)
    branch = models.ForeignKey('Branch',on_delete=models.CASCADE,related_name='contacts')



