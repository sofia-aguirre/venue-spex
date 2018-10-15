from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class CustomUser(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True, null=True)
    full_name = models.CharField(max_length=100)
    contact_email = models.CharField(max_length=100)
    contact_phone = models.IntegerField()

    def __str__(self):
        return self.full_name

class Venue(models.Model):
    # basic venue details
    manager = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="venue")
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    parking_diagram = models.ImageField(upload_to='parking_diagram',blank=True, null=True)
    parking_details = models.TextField()
    # audience/house space
    audience_diagram = models.ImageField(upload_to='audience_diagram',blank=True, null=True)
    audience_details= models.TextField()
    # sound department
    sound_diagram = models.ImageField(upload_to='sound_diagram',blank=True, null=True)
    houseSoundInstalled = models.TextField()
    houseSoundAvail = models.TextField()
    # electric department
    electrics_diagram = models.ImageField(upload_to='electrics_diagram',blank=True, null=True)
    houseElectricInstalled = models.TextField()
    houseElectricAvail = models.TextField()
    # lights department
    lights_diagram = models.ImageField(upload_to='lights_diagram',blank=True, null=True)
    houseLightsInstalled = models.TextField()
    houseLightsAvail = models.TextField()
    # stage department
    stage_diagram = models.ImageField(upload_to='stage_diagram',blank=True, null=True)
    houseStageInstalled = models.TextField()
    houseStageAvail = models.TextField()
    # artist accommodations / storage department
    backstage_diagram = models.ImageField(upload_to='backstage_diagram',blank=True, null=True)
    houseBackInstalled = models.TextField()
    houseBackAvail = models.TextField()

    def __str__(self):
        return self.title


