from django.shortcuts import render
from .forms import FeedbackForm

# Create your views here.
def feedback_form(request,user_id):
    request.META["CSRF_COOKIE_USED"] = True
    current_user_id = int(user_id)
    return render(request,'feedback.html',{'user_id':user_id})

def save_feedback(request):
	if request.method == 'POST':
		is_success = False
		feedback_form = FeedbackForm(request.POST)
		if feedback_form.is_valid():
			feedback_form.save();
			is_success = True
			return render(request,'feedback_thanks.html')
		return render(request,'feedback.html',{'feedback_form':feedback_form})
