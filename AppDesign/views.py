from django.shortcuts import render
from django.contrib.auth.views import LoginView



def index(request):
    return render(request, 'catalog/index.html')

class BBLoginView(LoginView):
    template_name = 'catalog/login.html'

