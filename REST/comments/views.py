from django.shortcuts import render
from rest_framework.response import Response
from rests.models import Book
from .models import Comment
from rest_framework.views import APIView
from .serializer import BookDetailSerializer, CommentSerializer,CommentCreteSerializer
from rest_framework import status
# Create your views here.

class BookDetailView(APIView):

    def get(self,request,*args,**kwargs):
        try:
            book = Book.objects.get(id=kwargs['book_id'])
        except Book.DoesNotExist:
            return Response({"data":"NotFound"},status=status.HTTP_404_NOT_FOUND)
        serializer = BookDetailSerializer(book)
        return Response(serializer.data)


    def post(self,request,*args,**kwargs):
        serializer = CommentCreteSerializer(data=request.data)
        if serializer.is_valid():
            book = Book.objects.get(id=kwargs['book_id'])
            text = serializer.data.get('text')
            Comment.objects.create(book=book,text=text,user=request.user)
            return Response({"data":"comment create successfully"})
        return Response(serializer.errors)
