from django.shortcuts import render
from rest_framework import generics
from .serializers import PizzeriaListSerializer, PizzeriaDetailSerializer
# Create your views here.
from .models import Pizzeria
#from .send_mail import send_email

class PizzeriaListAPIView(generics.ListAPIView):
    queryset = Pizzeria.objects.all()
    serializer_class = PizzeriaListSerializer 

class PizzeriaRetrieveAPIView(generics.RetrieveAPIView):
    lookup_field = "id"
    queryset = Pizzeria.objects.all()
    serializer_class = PizzeriaDetailSerializer 

class PizzeriaCreateAPIView(generics.CreateAPIView):
    queryset = Pizzeria.objects.all()
    serializer_class = PizzeriaDetailSerializer 
    #send_email()


class PizzeriaRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    lookup_field = "id"
    queryset = Pizzeria.objects.all()
    serializer_class = PizzeriaDetailSerializer 

class PizzeriaDestroyAPIView(generics.DestroyAPIView):
    lookup_field = "id"
    queryset = Pizzeria.objects.all()



