from django.db import models
from django.core.validators import RegexValidator,EmailValidator
import json

# Create your models here.

class Feedback(models.Model):
    alphanumeric_validator = RegexValidator(r'^[A-Za-z0-9]*$','Shall Contain only alphabets and numbers')
    alphabet_validator = RegexValidator(r'^[A-Za-z0-9]$','Shall contain only alphabets')
    email_validator = EmailValidator(message = 'Please check the email address')
    # Regex Reference : https://stackoverflow.com/questions/3868753/find-phone-numbers-in-python-script
    phone_validator = RegexValidator(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})','Please check your phone number')


    feedback_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('profile.Profile',on_delete=models.CASCADE)
    apartment_name = models.CharField(max_length=50,validators=[alphanumeric_validator])
    description = models.CharField(max_length=400,validators=[alphanumeric_validator])
    rating = models.IntegerField(default=1)
