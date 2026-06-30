from django.shortcuts import render,redirect
from . models import todoapp
# Create your views here.
def index(request):
    todo=todoapp.objects.all()
    return render(request,'index.html',{'todo':todo}) 

def add_task(request):
    if request.method=='POST':
        a=request.POST.get('task-name')
        b=request.POST.get('task-date')
        todoapp.objects.create(taskname=a,date=b)
        return redirect('home')
    return render(request,'add_task.html')

def delete_task(request,id):
    a=todoapp.objects.filter(id=id)
    a.delete()
    return redirect('home')
    
def update_task(request,id):
    a=todoapp.objects.get(id=id)
    if request.method=='POST':
        a.taskname=request.POST.get('Task-name') 
        a.date=request.POST.get('task-date') 
        a.save()
        return redirect('home')
    return render(request,'update.html',{'a':a})


