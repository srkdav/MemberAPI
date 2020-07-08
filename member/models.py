from django.db import models

#Customer Model And ActivityPeriod Model.
class Customer(models.Model):
    cust_id = models.CharField(primary_key=True,max_length=200)
    real_name = models.CharField(max_length=200,null=True)
    tz = models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.real_name

class ActivityPeriod(models.Model):
    # activity_id = models.IntegerField(primary_key=True)
    start_time=models.DateTimeField()
    end_time=models.DateTimeField()
    cust_id= models.ForeignKey(Customer,related_name="activity",on_delete=models.CASCADE) 
    