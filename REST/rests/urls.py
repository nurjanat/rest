from django.urls import path,include
from .views import *
from rest_framework import routers
# path views generics
# router ViewSets


router = routers.DefaultRouter()
router.register('order_set',OrderModelViewSet)
router.register('books',BookView)

urlpatterns = [
    path('users/',UserView.as_view()),
    path('my_orders/',MyOrderAPIView.as_view()),
    path('authors/',AuthorView.as_view()),
    path('order/',OrderAPIView.as_view()),
    path('order/<int:order_id>/',ModifyOrder.as_view()),
    path('book_demo/<str:abbr>/',BookDemoView.as_view()),
    path('',include(router.urls)),
    path('branches/',BranchAPIView.as_view()),
    path('contacts/',ContactAPIView.as_view())
]



