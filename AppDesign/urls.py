from django.urls import path
from .views import index, BBLoginView

app_name = 'AppDesign'

urlpatterns = [
    path('', index, name='index'),
    path('accounts/login', BBLoginView.as_view(), name='login'),
]
