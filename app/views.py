from django.shortcuts import render
from rest_framework import viewsets

from app.models import Passport
from app.serializers import PassportSerializer


class PassportViewSet(viewsets.ModelViewSet):
    queryset = Passport.objects.all()
    serializer_class = PassportSerializer
