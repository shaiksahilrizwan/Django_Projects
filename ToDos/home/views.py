from django.shortcuts import render
from .models import Task
# Create your views here.
def home(request):
  param={'error':''}
  if request.method=="POST":
    pass
    title=request.POST.get('title')
    desc=request.POST.get('desc')
    auth=request.POST.get('auth')
    print(title,desc,auth)
    if(str(auth)=="None" or str(title)=='None' or str(desc)=='None'):
      param={"error":"Check The Authentication/Fields Can't be empty"}
      return render(request,'home.html',param)
    else:
      param={'error':'Tasks Saved'}
      ins=Task(task_title=title,taskDesc=desc)
      ins.save()
      return render(request,'home.html',param)  
    
  return render(request,'home.html')
def about(request):
  return render(request,'about.html')
def task(request):
  allTasks=Task.objects.all()
  context={'tasks':allTasks}
  return render(request,'tasks.html',context)