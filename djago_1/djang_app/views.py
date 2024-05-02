from django.shortcuts import render
from .models import school
from .forms import schoolForm
# Create your views here.
def home (request):
    if request.POST:
        frm = schoolForm(request.POST, request.FILES)
        if frm.is_valid():
            frm.save()
    else:
        frm = schoolForm()

    return render(request,'index.html',{'frm':frm})

def view(request):
    orm = school.objects.all()
 
    return render(request,'list.html',{'orm':orm})

def edit(request,pk):
    edt = school.objects.get(pk=pk)
    if request.POST:
        frm = schoolForm(request.POST,request.FILES, instance=edt)
        if frm.is_valid():
            edt.save()
    else:
        frm = schoolForm(instance=edt)

    return render(request,'edit.html',{'frm':frm})

def delete (request,pk):
    delf=school.objects.get(pk=pk)
    delf.delete()
    orm= school.objects.all()
    return render(request,'list.html',{'orm':orm})
    
