from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm

def home(request):
	return render(request,'halls/home.html')
# Create your views here.

class SignUp(generic.CreateView):
	form_class = UserCreationForm
	success_url = reverse_lazy('home')
	template_name = 'registration/signup.html' # must have this name unless changed
