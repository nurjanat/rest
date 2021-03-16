from django.urls import path, include

from . import views
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register('register',RegisterView)


urlpatterns = [
    path('register/',include(router.urls)),
    path('signup/',SignupView.as_view()),
    path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            activate, name='activate'),
]