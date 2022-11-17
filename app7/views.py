from django.shortcuts import render,redirect
from django.http import HttpResponse
from . forms import Table1Form,LoginForm,UpdateForm,ChangePasswordForm,GalleryForm
from . models import Table1,Gallery
from django.contrib import messages
from django.contrib.auth import logout as logouts
# Create your views here.
def hello(request):
    return HttpResponse("django pro")
def index(request):
    element="TITANIUM"
    return render(request,'index.html',{'data':element})

# def register(request):
#     form=Table1Form()
#     return render(request,'register.html',{'data':form})

def register(request):
    if request.method=='POST':
        form=Table1Form(request.POST)
        if form.is_valid():
            name=form.cleaned_data['Name']
            age=form.cleaned_data['Age']
            place=form.cleaned_data['Place']
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']
            confirmpassword=form.cleaned_data['ConfirmPassword']

            user=Table1.objects.filter(Email=email).exists()

            if user:
                messages.warning(request,"user already exist")
                return redirect('/register')
            elif password!=confirmpassword:
                messages.warning(request,"password mismatch")
                return redirect('/register')
            else:
                tab=Table1(Name=name,Age=age,Place=place,Email=email,Password=password)
            
            tab.save()
            messages.success(request,"registration successful")
            return redirect('/')
    else:
        form=Table1Form()
    return render(request,'register.html',{'data':form})

def login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']
            

            user=Table1.objects.get(Email=email)

            if not user:
                messages.warning(request,"user does not exist")
                return redirect('/login')
            elif password!=user.Password:
                messages.warning(request,"password incorrect")
                return redirect('/login')
            else:
                messages.success(request,"login successful")
                return redirect('/home/%s' % user.id )
    else:
        form=LoginForm()
    return render(request,'login.html',{'data':form})

def home(request,id):
    user=Table1.objects.get(id=id)
    return render(request,'home.html',{'data':user})

def show_users(request):
    users=Table1.objects.all()
    return render(request,'show_users.html',{'data':users})

def update(request,id):
    user=Table1.objects.get(id=id)
    if request.method=='POST':
        form=UpdateForm(request.POST or None,instance=user)
        if form.is_valid():
            form.save()
            messages.success(request,"update successful")
            return redirect('/home/%s' % user.id)
    else:
        form=UpdateForm(instance=user)
    return render(request,'update.html',{'data':form,'user':user})

def delete(request,id):
    user=Table1.objects.get(id=id)
    user.delete()
    messages.success(request,"user deleted successfully")
    return redirect('/')

def changepassword(request,id):
    user=Table1.objects.get(id=id)
    if request.method=='POST':
        form=ChangePasswordForm(request.POST)
        if form.is_valid():
            oldpassword=form.cleaned_data['OldPassword']
            newpassword=form.cleaned_data['NewPassword']
            confirmpassword=form.cleaned_data['ConfirmPassword']
            
            if oldpassword!=user.Password:
                messages.warning(request,"password incorrect")
                return redirect('/changepassword/%s' % user.id)
            elif newpassword==oldpassword:
                messages.warning(request,"Old and new password looks similar")
                return redirect('/changepassword/%s' % user.id)
            elif newpassword!=confirmpassword:
                messages.warning(request,"Password mismatch")
                return redirect('/changepassword/%s' % user.id)
            else:
                user.Password=newpassword
                user.save()
                messages.success(request,"Password changed successfully")
                return redirect('/home/%s' % user.id)
    else:
    
        form=ChangePasswordForm()
    return render(request,'changepassword.html',{'data':form})

def logout(request):
    logouts(request)
    messages.success(request,"Logout Successful")
    return redirect('/')

def gallery(request):
    if request.method=='POST':
        form=GalleryForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            photo=form.cleaned_data['Photo']
            name=form.cleaned_data['Name']
            age=form.cleaned_data['Age']
            place=form.cleaned_data['Place']
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']
            confirmpassword=form.cleaned_data['ConfirmPassword']
            

            user=Table1.objects.filter(Email=email).exists()

            if user:
                messages.warning(request,"user already exists")
                return redirect('/register')
            elif password!=confirmpassword:
                messages.warning(request,"password mismatch")
                return redirect('/register')
            else:
                tab=Gallery(Photo=photo,Name=name,Age=age,Place=place,Email=email,Password=password)
                tab.save()
                messages.success(request,"registration successful")
                return redirect('/')
    else:
        form=GalleryForm()
        return render(request,'gallery.html',{'data':form})

def display(request):
    gallery=Gallery.objects.all()
    return render(request,'display.html',{'data':gallery})