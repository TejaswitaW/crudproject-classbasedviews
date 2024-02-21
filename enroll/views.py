from typing import Any, Dict, Optional
from django.shortcuts import render,HttpResponseRedirect
from django.views.generic.base import TemplateView,RedirectView
from django.views import View
from .forms import StudentRegistration
from .models import User

# Create your views here.

class UserAddShowView(TemplateView):
    template_name = 'enroll/addandshow.html'
    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(**kwargs)
        fm = StudentRegistration()
        st = User.objects.all()
        context = {'students':st,'form':fm}
        return context
    def post(self,request):
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            user = User(name=name,email=email,password=password)
            user.save()
        return HttpResponseRedirect('/')

'''
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
'''

class UserUpdateView(View):
    def get(self,request,id):
        usr = User.objects.get(pk=id)
        fm = StudentRegistration(instance=usr)
        return render(request,'enroll/updatestudent.html',{'form':fm})
    def post(self,request,id):
        usr = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST,instance=usr)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect('/')

'''
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

    return render(request,'enroll/updatestudent.html',{'form':fm})'''

class USerDeleteView(RedirectView):
    url = '/'
    def get_redirect_url(self,*args,**kwargs):
        # print(kwargs)
        del_id = kwargs['id']
        User.objects.get(pk=del_id).delete()
        # print("Here: ",super().get_redirect_url(*args,**kwargs))
        return super().get_redirect_url(*args,**kwargs)


'''
def delete_data(request,id):
    """
    This function delete user from the database.
    """
    if request.method == 'POST':
        usr = User.objects.get(pk=id)
        usr.delete()
        return HttpResponseRedirect('/')
        '''
    