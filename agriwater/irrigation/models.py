from django.db import models
from django.contrib.auth.models import User

class IrrigationRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    moisture = models.FloatField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    prediction = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
