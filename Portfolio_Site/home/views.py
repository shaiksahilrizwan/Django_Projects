from django.shortcuts import render
from . models import Contact 
# Create your views here.
def home(request):
  return render(request,'home.html')
def about(request):
  return render(request,'about.html')
def contact(request):
  if request.method=="POST":
    name=request.POST['name']
    email=request.POST['email']
    phone=request.POST['phone']
    about=request.POST['about']
    print(name,email,phone,about)
    ins=Contact(name=name,email=email,phone=phone,about=about)
    ins.save()
  return render(request,'contact.html')
def projects(request):
  return render(request,'projects.html')