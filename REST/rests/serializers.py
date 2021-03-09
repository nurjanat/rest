from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ['id','title','description','year']


class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True)
    class Meta:
        model = Author
        fields = ['id','date_birth','date_death','country','bio','name','books']


    def create(self,validated_data):
        books_data = validated_data.pop('books')
        author = Author.objects.create(**validated_data)
        for book in books_data:
            Book.objects.create(author=author,**book)
        return author


class OrderSerializer(serializers.ModelSerializer):
    # book = serializers.StringRelatedField()
    status = serializers.CharField(read_only=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # total = 0
    class Meta:
        model = Order
        fields = ['id', 'user', 'address','book','quantity','data','status']




class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ['id','types','info']



class BranchSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(many=True)
    class Meta:
        model = Branch
        fields = ['id','name','contacts']
