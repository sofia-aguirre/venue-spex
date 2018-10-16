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
    contact_phone = models.CharField(max_length=17)

    def __str__(self):
        return self.full_name

class Venue(models.Model):
    # basic venue details
    manager = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="venue")
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    parking_diagram = models.ImageField(upload_to='parking_diagrams',blank=True, null=True)
    parking_details = models.TextField(blank=True)
    # audience/house space
    audience_diagram = models.ImageField(upload_to='audience_diagrams',blank=True, null=True)
    audience_details= models.TextField(blank=True)
    # sound department
    sound_diagram = models.ImageField(upload_to='sound_diagrams',blank=True, null=True)
    houseSoundInstalled = models.TextField(blank=True)
    houseSoundAvail = models.TextField(blank=True)
    # electric department
    electrics_diagram = models.ImageField(upload_to='electrics_diagrams',blank=True, null=True)
    houseElectricInstalled = models.TextField(blank=True)
    houseElectricAvail = models.TextField(blank=True)
    # lights department
    lights_diagram = models.ImageField(upload_to='lights_diagrams',blank=True, null=True)
    houseLightsInstalled = models.TextField(blank=True)
    houseLightsAvail = models.TextField(blank=True)
    # stage department
    stage_diagram = models.ImageField(upload_to='stage_diagrams',blank=True, null=True)
    houseStageInstalled = models.TextField(blank=True)
    houseStageAvail = models.TextField(blank=True)
    # artist accommodations / storage department
    backstage_diagram = models.ImageField(upload_to='backstage_diagrams',blank=True, null=True)
    houseBackInstalled = models.TextField(blank=True)
    houseBackAvail = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    commenter = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="comment")
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name="comment")
    comment_pic = models.ImageField(upload_to='comment_pics',blank=True, null=True)
    title = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.title