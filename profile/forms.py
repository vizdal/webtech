from django import forms
from profile.models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
    #first_name = forms.CharField(label='First Name',max_length=100)
    #last_name = forms.CharField(label='Last Name',max_length=100)
    #gender = forms.ChoiceField(choices=Profile.gender_options)
    #email = forms.EmailField()
    #phone = forms.RegexField(regex=r'^\+?1?\d{9,15}$')#, error_message = ("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."))
    #university = forms.CharField(label='University Name',max_length=100)
    #branch = forms.CharField(label='Branch Name',max_length=100)
    #is_veg = forms.ChoiceField(choices=Profile.meal_options)
    #is_smoke = forms.ChoiceField(choices=Profile.smoke_options)
    #is_alcohol = forms.ChoiceField(choices=Profile.alcohol_options)
    #profile_image = forms.ImageField()
