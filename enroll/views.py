from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistration
from .models import User

# Create your views here.

def add_show(request):
    """
    This function adds new user and show all users in the database.
    """
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            user = User(name=name,email=email,password=password)
            user.save()
            # after data get saved blank form should be visible
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    st = User.objects.all()
    return render(request,'enroll/addandshow.html',{'form':fm,'students':st})


def update_data(request,id):
    """
    This function update/edit user data.
    """
    if request.method == 'POST':
        usr = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST,instance=usr)
        if fm.is_valid():
            fm.save()
    else:
        usr = User.objects.get(pk=id)
        fm = StudentRegistration(instance=usr)

    return render(request,'enroll/updatestudent.html',{'form':fm})


def delete_data(request,id):
    """
    This function delete user from the database.
    """
    if request.method == 'POST':
        usr = User.objects.get(pk=id)
        usr.delete()
        return HttpResponseRedirect('/')
    