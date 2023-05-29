from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages
from .forms import StudentRegistration
from .models import User
from django.contrib.auth.forms import AuthenticationForm 
from django.shortcuts import redirect
# Create your views here.

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("add-show")
            else:
                messages.error(request, "User not approved.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


# This Function will Add new item and show all the items
def add_show(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            jt = fm.cleaned_data['jobtype']
            sl = fm.cleaned_data['salary']
            reg = User(name=nm, email=em, password=pw, jobtype=jt, salary = sl)
            reg.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'addandshow.html', {
        'form': fm,
        'stu': stud,
    })



def add_employee(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['username']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            jt = fm.cleaned_data['jobtype']
            sl = fm.cleaned_data['salary']
            reg = User(username=nm, email=em, password=pw, jobtype=jt, salary = sl)
            reg.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    return render(request, 'addEmployee.html', {
        'form': fm,
    })
# This Function will Update/Edit


def update_data(request, id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render(request, 'updateStudent.html', {
        'form': fm,
        'id': id,
    })


# This Function will delete the user
def delete_data(request, id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect("/")
