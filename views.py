from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import submit_feedback
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def body(request):
    return render(request, 'body.html')

def timeline(request):
    return render(request, 'timeline.html')

def feedback(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        feedback_text = request.POST.get('feedback')
        feedback_instance = submit_feedback(name = name, email = email, feedback = feedback_text, date = datetime.today())
        feedback_instance.save()
        messages.success(request, 'Success! Your data has been submitted.')
        return render(request, 'feedback.html')
    
def contact(request):
    return render(request, 'contact.html')

def end(request):
    return render(request, 'end.html')