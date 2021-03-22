from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import *

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    class Meta:
        model = Book
        fields = ['id','title','price','year','author','abbr']



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
    promo = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'user', 'address','book','quantity','data','status',
                  'total_price','payment_type','promocode','promo']


    def get_promo(self,obj):
        promocode = 'nurja'
        if obj.promocode == promocode:
            obj.total_sum -= 100
            obj.save()




    def get_total_price(self,obj):

        total_price = 0
        try:
            total_price += obj.quantity * obj.book.price
            if obj.address is None:
                obj.address = obj.user.profile.address
            obj.total_sum = total_price
            if obj.payment_type == 'card':
                if obj.user.profile.wallet >= total_price:
                    obj.user.profile.wallet -= total_price
                    obj.user.profile.save()
                    obj.save()
                else:
                    obj.delete()
                    raise ValidationError('Not Enough money!')
            else:
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




