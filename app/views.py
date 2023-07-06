from django.shortcuts import render, redirect

# Create your views here.
from app.form import TodoForm
from app.models import NoteBook


def todohomepage(request):
    return render(request, 'index.html')


def addtodo(request):
    form = TodoForm()
    if request.method == 'POST':
        data = TodoForm(request.POST)
        if data.is_valid():
            data.save()
            return redirect('todohomepage')
    return render(request, 'todo.html', {'form': form})

def viewtodo(request):
    data = NoteBook.objects.all()
    return render(request,'viewtodo.html',{'data' : data})

def updatetodo(request,id):
    data=NoteBook.objects.get(id=id)
    form=TodoForm(instance=data)
    if request.method=='POST':
        form=TodoForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect(viewtodo)
    return render(request,'todo.html',{'form':form})

def deletetodo(request,id):
    NoteBook.objects.get(id=id).delete()
    return redirect(viewtodo)