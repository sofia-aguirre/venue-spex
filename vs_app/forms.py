from django import forms
from django.forms import ModelForm
from .models import Venue, CustomUser, Comment
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','password','email', )

class CustomUserForm(ModelForm):

    class Meta():
        model = CustomUser
        fields = ('profile_pic', 'full_name', 'contact_email', 'contact_phone', )

class VenueForm(ModelForm):

    class Meta:
        model = Venue
        fields = ('title', 'location', 'venue_pic', 'parking_diagram',
        'parking_details', 'audience_diagram', 'audience_details', 
        'houseSoundInstalled','houseSoundAvail', 'sound_diagram', 
        'houseElectricInstalled', 'houseElectricAvail', 'electrics_diagram',
        'houseLightsInstalled', 'houseLightsAvail', 'lights_diagram',
        'houseStageInstalled', 'houseStageAvail', 'stage_diagram',
        'houseBackInstalled', 'houseBackAvail','backstage_diagram',)
        # widgets = {}

class CommentForm(ModelForm):

    class Meta():
        model = Comment
        fields = ('comment_pic', 'title', 'body', 'venue' )