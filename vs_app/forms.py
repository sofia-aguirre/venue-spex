from django import forms
from django.forms import ModelForm
from .models import Venue, CustomUser
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
        fields = ('title', 'location', 'houseSoundInstalled', 
        'houseElectricInstalled', 'houseLightsInstalled', 'houseStageInstalled', 
        'houseBackInstalled', 'houseSoundAvail', 'houseElectricAvail',
        'houseLightsAvail', 'houseStageAvail', 'houseBackAvail')
        # widgets = {
        #     'challange_date': DateInput(),
        #     'challange_time': TimeInput(),
        # }

