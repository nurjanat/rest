from django.urls import path,include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('order_set',OrderModelViewSet)

urlpatterns = [
    path('users/',UserView.as_view()),
    path('books/',BookView.as_view()),
    path('my_orders/',MyOrderAPIView.as_view()),
    path('authors/',AuthorView.as_view()),
    path('order/',OrderAPIView.as_view()),
    path('',include(router.urls)),
    path('branches/',BranchAPIView.as_view()),
    path('contacts/',ContactAPIView.as_view())
]