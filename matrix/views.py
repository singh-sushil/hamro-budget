from .forms import sign_up,official_login,user_login
from .models import signup,local_bodies_id,Node
from django.shortcuts import render,redirect
from django.http import HttpResponse ,HttpResponseRedirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate
from django.forms import ModelForm 

# Create your views here.
def home(request):
    form = sign_up()
    return render(request,'home.html', {'forms':form})


def register(request):
    return render(request,'register.html',{})


def cregister(request):
    if request.method == 'POST':
        if request.POST['password1'] != request.POST['password2']:
            messages.info(request,"password not matched")
            return redirect('/cregister/')
        else:
            if signup.objects.filter(username = request.POST['username']):
                messages.info(request,"username already taken")
                return redirect("/cregister/")
            else:
                form = sign_up(request.POST or None ,request.FILES or None)
                if form.is_valid():
                    instance = form.save(commit=False)
                    instance.save()
                    print("uploaded")
                    return redirect('/')
                else:
                    return redirect("/cregister/")
    else:
        form = sign_up()
    return render(request,'cregister.html',{'forms':form})

def officiallogin(request):
    if request.method == 'POST':
            if local_bodies_id.objects.filter(username = request.POST['username'],password = request.POST['password']):
                username = request.POST['username']
                page = username+'.html'
                print(page)
                return render(request,'{}'.format(page),{}) 
            else:
                messages.info(request,"username or password not matched")
                return redirect("/official-login/")
    else:
        form = official_login()
    return render(request,'ologin.html',{'forms':form})

def userlogin(request):
    if request.method == 'POST':
            if signup.objects.filter(username = request.POST['username'],password = request.POST['password']):
                #page = username+'.html'
                #print(page)
                #return render(request,'{}'.format(page),{}) 
                return render(request,'local1.html',{})
            else:
                messages.info(request,"username or password not matched")
                return redirect("/user-login/")
    else:
        form = user_login()
    return render(request,'ulogin.html',{'forms':form})



def search(request):
    if request.method == 'GET':
        body = Node.objects.filter(body__regex = r'{}+'.format(request.GET['name']))
    else:
        alldoctor = dr_register.objects.all()
    
    context = {
        'bodies':body
    }

    return render(request,'search.html',context)

    