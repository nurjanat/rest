from rest_framework.fields import CharField

from .models import Comment
from rests.models import Book
from rest_framework.serializers import ModelSerializer,Serializer

class CommentSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'




class CommentCreteSerializer(Serializer):
    text = CharField(allow_blank=False)



class BookDetailSerializer(ModelSerializer):

    comment_set = CommentSerializer(many=True)

    class Meta:
        model = Book
        fields = ['id','title','description','price','year','author','comment_set']



