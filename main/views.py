from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def home(request):
    return render(request, 'home.html')


#User register
def register(request):
    form = UserCreationForm
    if request.method == 'POST':
        reg_form = UserCreationForm(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            messages.success(request, "User successfully registered.")
    return render(request, 'registration/register.html', {'form': form})
