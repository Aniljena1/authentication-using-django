from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import SignupForm
from django.http import HttpResponseRedirect

def home_page_view(request):
    return render(request,'myapp/home.html')

@login_required
def java_exams_view(request):
    return render(request,'myapp/java.html')

def python_exams_view(request):
    return render(request,'myapp/python.html')

def apptitude_exams_view(request):
    return render(request,'myapp/apptitude.html')

def Logout_view(request):
    return render(request,'myapp/logout.html')

def Signup_view(request):
    form=SignupForm()
    if request.method=='POST':
        form=SignupForm(request.POST)
        form.save()
        return HttpResponseRedirect('/accounts/login')



    return render(request,'myapp/signup.html',{'form':form})