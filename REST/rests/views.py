from django.utils import timezone
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, status
from .serializers import *
from rest_framework import views
from datetime import date
from rest_framework import filters
from rest_framework import permissions
# Create your views here.

class UserView(views.APIView):

    def get(self,request,*args,**kwargs):
        users = User.objects.all()


        serializer = UserSerializer(users,many=True)
        return Response(serializer.data)



class BookView(viewsets.ModelViewSet):
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['title','price']

    # def get(self,request,*args,**kwargs):
    #     books = Book.objects.all()
    #
    #     serializer = BookSerializer(books,many=True)
    #     return Response(serializer.data)
    #
    # def post(self,request,*args,**kwargs):
    #     serializer = BookSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'data':'Ok'})


class AuthorView(views.APIView):

    def get(self,request,*args,**kwargs):
        authors = Author.objects.all()

        serializer = AuthorSerializer(authors,many=True)
        return Response(serializer.data)


    def post(self,request,*args,**kwargs):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':'Ok'})
        return Response(serializer.errors)


class OrderAPIView(views.APIView):


    def post(self,request,*args,**kwargs):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

class ModifyOrder(views.APIView):

    def put(self,request,*args,**kwargs):
        order = Order.objects.get(id=kwargs['order_id'])
        hours = timezone.now().hour * 60 # hours converted to minutes
        minutes = timezone.now().minute #minutes
        result1 = hours + minutes
        result2 = (order.data.hour * 60) + order.data.minute
        serializer = OrderSerializer(order,data=request.data)
        print()
        if serializer.is_valid():
            if abs(result1 - result2) <= 5:
                serializer.save()
                return Response({'data':'ok'})
            else:
                return Response({"data":"Time is up!"})
        return Response(serializer.errors)



    # def delete(self,request,order_id):
    #     order = Order.objects.get(id=order_id)
    #     order.delete()
    #     return Response({'data':'successfully deleted'})








class MyOrderAPIView(views.APIView):

    def get(self,request,*args,**kwargs):
        orders = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(orders,many=True)
        return Response(serializer.data)


class OrderModelViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class BranchAPIView(views.APIView):
    def get(self,request,*args,**kwargs):
        branches = Branch.objects.all()
        serializer = BranchSerializer(branches,many=True)
        return Response(serializer.data)


    def post(self,request,*args,**kwargs):
        serializer = BranchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


class ContactAPIView(views.APIView):
    def get(self,request,*args,**kwargs):
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts,many=True)
        return Response(serializer.data)


    def post(self,request,*args,**kwargs):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)




class BookDemoView(views.APIView):

    def get(self,request,*args,**kwargs):
        try:
            book = Book.objects.get(abbr=kwargs['abbr'])
        except Book.DoesNotExist:
            return Response({'data':'Book not found'},status=status.HTTP_404_NOT_FOUND)
        demo = book.book_file.open()
        return Response({'demo':demo.read()[:5]})