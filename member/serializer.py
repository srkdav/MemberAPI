from rest_framework import serializers

from .models import *

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPeriod
        fields = ('start_time','end_time','cust_id')

class CustomerSerializer(serializers.ModelSerializer):
    activity = ActivitySerializer(read_only=True,many=True)
    class Meta:
        model = Customer
        fields = ('cust_id','real_name','tz','activity')