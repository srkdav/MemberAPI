from django.shortcuts import render
from rest_framework import viewsets

from .serializer import CustomerSerializer,ActivitySerializer
from .models import *

# Create your views here.
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
  
    def get_serializer(self, *args, **kwargs):
        if "data" in kwargs:
            data = kwargs["data"]

        # check if many is required
            if isinstance(data, list):
                kwargs["many"] = True

        return super(CustomerViewSet, self).get_serializer(*args, **kwargs)

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = ActivityPeriod.objects.all()
    serializer_class = ActivitySerializer
    def get_serializer(self, *args, **kwargs):
        if "data" in kwargs:
            data = kwargs["data"]

        # check if many is required
            if isinstance(data, list):
                kwargs["many"] = True

        return super(ActivityViewSet, self).get_serializer(*args, **kwargs)
