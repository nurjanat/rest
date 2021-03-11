from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    class Meta:
        model = Book
        fields = ['id','title','price','year','author']


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
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    total_price = serializers.SerializerMethodField()


    class Meta:
        model = Order
        fields = ['id', 'user', 'address','book','quantity','data','status','total_price']

    def get_total_price(self,obj):

        total_price = 0
        try:
            total_price += obj.quantity * obj.book.price
            obj.total_price = total_price
            obj.save()
            return total_price
        except AttributeError:
            return 0



class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ['id','types','info']



class BranchSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(many=True)
    class Meta:
        model = Branch
        fields = ['id','name','contacts']




    def create(self,validated_data):
        contacts_data = validated_data.pop('contacts')
        branch = Branch.objects.create(**validated_data)
        for contact in contacts_data:
            Contact.objects.create(branch=branch,**contact)
        return branch
