from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class opinion(models.Model):
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=1000)
    posted_date_time = models.DateTimeField()
