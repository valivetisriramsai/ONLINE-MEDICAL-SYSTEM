from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    is_patient=models.BooleanField(default=False)
    mobile_number=models.TextField(blank=True)
    age=models.IntegerField(default=0)
    fee=models.IntegerField(default=0)
    Qualification=models.TextField(blank=True)
    Experience=models.IntegerField(default=0)

class doctors(models.Model):
    name=models.TextField(blank=True)
    mobile_number=models.TextField(blank=True)
    email=models.TextField(blank=True)
    age=models.IntegerField(default=0)
    user_image=models.ImageField(upload_to='media/',default=None)
    fee=models.IntegerField(default=0)
    Qualification=models.TextField(blank=True)
    Experience=models.IntegerField(default=0)
    
    
class appointments(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE);
    doctor=models.ForeignKey(doctors,on_delete=models.CASCADE);
    time=models.DateTimeField(auto_now_add=False)
    
    
    
    