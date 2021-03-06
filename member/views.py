from django.shortcuts import render
from rest_framework import viewsets

from .serializer import CustomerSerializer,ActivitySerializer
from .models import *

# Customer View and Activity View.
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
  
  #to ensure list of objects can be sent by POST not just an object alone.
    def get_serializer(self, *args, **kwargs):
        if "data" in kwargs:
            data = kwargs["data"]
            if isinstance(data, list):
                kwargs["many"] = True

        return super(CustomerViewSet, self).get_serializer(*args, **kwargs)

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = ActivityPeriod.objects.all()
    serializer_class = ActivitySerializer
    
    #to ensure list of objects can be sent by POST not just an object alone.
    def get_serializer(self, *args, **kwargs):
        if "data" in kwargs:
            data = kwargs["data"]
            if isinstance(data, list):
                kwargs["many"] = True

        return super(ActivityViewSet, self).get_serializer(*args, **kwargs)
