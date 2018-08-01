import os
from .forms import ProfileForm
from django.core import serializers
from django.core.validators import validate_email
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from profile.models import Profile
# Create your views here.`
#To load profile form
def profile_form(request,user_id):
    request.META["CSRF_COOKIE_USED"] = True
    current_user_id = int(user_id)
    user = Profile.objects.get(user_id=current_user_id)
    return render(request,'profile-edit.html',{'saved_row':user,'is_update':0})
#To upload image
def handle_uploaded_file(f,filename):
    with open(filename, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def update_profile(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST,request.FILES)
        if profile_form.is_valid():
            constructed_file_name = 'user.jpeg'
            email = profile_form.cleaned_data['email']
            user, created = Profile.objects.get_or_create(email=email)
            if not created:
                #Update the user if they already exists
                update_form = ProfileForm(request.POST,instance=user)
                if len(request.FILES) == 0:
                    update_form.profile_image = user.profile_image
                    filename, file_extension = os.path.splitext(user.profile_image.url)
                    constructed_file_name = str(user.user_id)+file_extension
                user = update_form.save()
            if len(request.FILES) != 0:
                filename, file_extension = os.path.splitext(request.FILES['profileimage'].name)
                constructed_file_name = str(user.user_id)+file_extension
                tot_path = 'pro_image/'+ constructed_file_name
                handle_uploaded_file(request.FILES['profileimage'],'static/'+tot_path)
                update_form = Profile.objects.get(email=user.email)
                update_form.profile_image = tot_path
                update_form.save()
            return HttpResponseRedirect("/profile/"+str(user.user_id))
            #return render(request,'profile.html', { 'saved_row':user,'is_update':1, 'file_name':constructed_file_name})
            #return render(request,'profile.html')
        else:
            user = None
            try:
                user = Profile.objects.get(email=request.POST.get('email'))
            except:
                print('Invalid Email Details Cannot be Loaded!')
            return render(request,'profile-edit.html',{'profile_form':profile_form,'saved_row':user,'is_update':1})
    else:
        return HttpResponse('bye')
#To get the user details given the user id
def get_profile_data(request,user_id):
   current_user_id = int(user_id)
   user_details = Profile.objects.get(user_id=current_user_id)
   return HttpResponse(serializers.serialize('json', [ user_details, ]))

def return_profile_page(request,user_id):
    current_user_id = int(user_id)
    user = Profile.objects.get(user_id=current_user_id)
    path,file_name = os.path.split(user.profile_image.url)
    return render(request,'profile.html', { 'saved_row':user,'is_update':1, 'file_name':file_name})

def validate_form_data(user):
    validate_email(user.email)
    #raise forms.ValidationError("Please check your email")