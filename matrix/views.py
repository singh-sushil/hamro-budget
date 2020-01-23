from django.shortcuts import render
from .forms import sign_up

# Create your views here.
def home(request):
    form = sign_up()
    return render(request,'home.html', {'forms':form})