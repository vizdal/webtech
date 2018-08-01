from django.db import models
from django.core.validators import RegexValidator,EmailValidator
import json

# Create your models here.

class Profile(models.Model):
    alphanumeric_validator = RegexValidator(r'^[A-Za-z0-9]*$','Shall Contain only alphabets and numbers')
    alphabet_validator = RegexValidator(r'^[A-Za-z0-9]$','Shall contain only alphabets')
    email_validator = EmailValidator(message = 'Please check the email address')
    # Regex Reference : https://stackoverflow.com/questions/3868753/find-phone-numbers-in-python-script
    phone_validator = RegexValidator(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})','Please check your phone number')

    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50,validators=[alphanumeric_validator])
    meal_options = (
        ('V','Vegetarian'),
        ('N','Non-Vegetarian')
    )
    last_name = models.CharField(max_length=50,validators=[alphanumeric_validator])
    gender_options = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
        ('N', 'Prefer Not to Mention')
    )
    smoke_options = (
        ('S','Smoker'),
        ('N','Non-Smoker')
    )

    alcohol_options = (
        ('A','Alcoholic'),
        ('N','Non-Alcoholic')
    )
    gender = models.CharField(max_length=1, choices=gender_options)
    email = models.EmailField(max_length=100,validators=[email_validator])
    phone = models.CharField(max_length=20,validators=[phone_validator])
    university = models.CharField(max_length=100,validators=[alphanumeric_validator])
    branch = models.CharField(max_length=70,validators=[alphanumeric_validator])
    is_veg = models.CharField(max_length=1, choices=meal_options)
    is_smoke = models.CharField(max_length=1, choices=smoke_options)
    is_alcohol = models.CharField(max_length=1, choices=alcohol_options)
    profile_image = models.ImageField(upload_to='images/', default='images/jpeg/user.jpg')

    def __str__():
        return_dict = {}
        return_dict['id'] = user_id
        return_dict['fname'] = first_name
        return_dict['lname'] = last_name
        return_dict['gender'] = gender
        return_dict['email'] = email
        return_dict['phone'] = phone
        return_dict['university'] = university
        return_dict['branch'] = branch
        return_dict['is_veg'] = is_veg
        return_dict['is_smoke'] = is_smoke
        return_dict['is_alcohol'] = is_alcohol
        return_dict['image_url'] = image_url
        return json.dumps(return_dict)

    def get_profile_details(user_id_param):
        return Profile.objects.filter(user_id=user_id_param)