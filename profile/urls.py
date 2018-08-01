from django.contrib import admin
from django.urls import include,path
from profile.views import profile_form,update_profile,get_profile_data,return_profile_page

urlpatterns = [
    path('<int:user_id>/edit/',profile_form,name="profile_form"),
    path('update_profile/',update_profile,name="Update Profile"),
    path('data/<int:user_id>/',get_profile_data,name="Profile Data"),
    path('<int:user_id>/',return_profile_page,name="Profile Page"),
]
