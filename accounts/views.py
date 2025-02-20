from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# for users
from django.contrib.auth.models import User
from django.contrib.auth import login


# Create your views here.
def signupaccount(request):
    if request.method == 'GET':
        return render(request, 'signupaccount.html', {'form' : UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
            user.save()
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'signupaccount.html',
                {'form' : UserCreationForm, 'error' : 'Passwords do not match'})