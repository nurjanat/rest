from rest_framework.fields import CharField, SerializerMethodField

from .models import Comment
from rests.models import Book
from rest_framework.serializers import ModelSerializer,Serializer
from estimate.serializer import RateModelSerializer


class CommentSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'




class CommentCreteSerializer(Serializer):
    text = CharField(allow_blank=False)



class BookDetailSerializer(ModelSerializer):
    rates = RateModelSerializer(many=True)
    comment_set = CommentSerializer(many=True)
    avg_rate = SerializerMethodField()
    class Meta:
        model = Book
        fields = ['id','title','description','price','year','author','comment_set','rates','avg_rate']

    def get_avg_rate(self,obj):
        total_star = 0
        for rate in obj.rates.all():
            total_star += rate.star
        return round(total_star/len(obj.rates.all()),1)








