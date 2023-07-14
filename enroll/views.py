from django.shortcuts import render
from .forms import StudentRegistration
from .models import User

# Create your views here.
def add_show(request):
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
    return render(request,'enroll/addandshow.html',{'form':fm})
