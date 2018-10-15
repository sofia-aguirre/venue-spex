from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class CustomUser(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    full_name = models.CharField(max_length=100)
    contact_email = models.CharField(max_length=100)
    contact_phone = models.IntegerField()

    def __str__(self):
        return self.full_name

class Venue(models.Model):
    title = models.CharField(max_length=100)
    manager = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="venue")
    location = models.CharField(max_length=100)
    houseSoundInstalled = models.TextField()
    houseElectricInstalled = models.TextField()
    houseLightsInstalled = models.TextField()
    houseStageInstalled = models.TextField()
    houseBackInstalled = models.TextField()
    houseSoundAvail = models.TextField()
    houseElectricAvail = models.TextField()
    houseLightsAvail = models.TextField()
    houseStageAvail = models.TextField()
    houseBackAvail = models.TextField()

    def __str__(self):
        return self.title


