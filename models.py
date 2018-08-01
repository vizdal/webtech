from django.db import models

class Profile(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    meal_options = (
        ('V','Vegetarian'),
        ('N','Non-Vegetarian')
    )
    last_name = models.CharField(max_length=50)
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
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    university = models.CharField(max_length=100)
    branch = models.CharField(max_length=70)
    is_veg = models.CharField(max_length=1, choices=meal_options)
    is_smoke = models.CharField(max_length=1, choices=smoke_options)
    is_alcohol = models.CharField(max_length=1, choices=alcohol_options)
    image_url = models.CharField(max_length=150)
