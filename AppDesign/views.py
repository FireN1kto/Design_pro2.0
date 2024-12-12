from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'catalog/index.html')

class BBLoginView(LoginView):
    template_name = 'catalog/login.html'

@login_required
def profile(request):
    return render(request, 'catalog/profile.html')

