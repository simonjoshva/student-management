from django.shortcuts import render,redirect
from apps.models import student
from apps.forms import studentform
def studentt(request):
    students=student.objects.all()
    return render(request,'students.html',{'s':students})
def insert(request):
    form=studentform()
    if request.method=='POST':
        form=studentform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
    return render(request,'insert.html',{'form':form})
def delete(request,id):
    students=student.objects.get(id=id)
    students.delete()
    return redirect('/home') 
def update(request,id):
    s=student.objects.get(id=id)
    if request.method=="POST":
        form=studentform(request.POST,instance=s)
        if form.is_valid():
            form.save()
        return redirect('/home')
    return render(request,'update.html',{'ss':s})

def search(request):
    search_id=request.GET.get('id')
    if search_id:
        students=student.objects.filter(id=search_id)
    else:
        students=student.objects.all()
    return render(request,'students.html',{'s':students})
# Create your views here

