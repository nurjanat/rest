from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage



class RegisterView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class SignupView(APIView):

    def post(self,request,*args,**kwargs):
        serializers = RegisterSerializer(data=request.data)
        if serializers.is_valid():
            user = serializers.save()
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('accounts/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = serializers.data['email']
            email = EmailMessage(
                mail_subject, message, to=[to_email,]
            )

            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
        return HttpResponse(serializers.errors)

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.is_staff = True
        user.save()
        login(request, user)
        return Response('Thank you for your email confirmation. Now you can login your account.')
    return Response({"NOT  OK!"})