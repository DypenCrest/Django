from django.shortcuts import render, HttpResponseRedirect
from .models import List

# Create your views here.

def shop_list(request,):
    lists=List.objects.all()
    return render(request,'shop_list.html',{'lists':lists})

def list_add(request):
    if request.method == "POST":
        List.objects.create(name=request.POST['name'])
        return HttpResponseRedirect('/')
    else:
        return render(request,'list_add.html')

def list_update(request,pk):
    list=List.objects.get(pk=pk)
    if request.method=="POST":
        list.name=request.POST['name']
        list.save()

        return HttpResponseRedirect('/')
    else:
        return render(request,'list_update.html',{'list':list})

def list_delete(request,pk):
    list=List.objects.get(pk=pk)
    list.delete()
    return HttpResponseRedirect('/')