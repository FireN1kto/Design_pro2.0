from django.urls import path
from .views import index, BBLoginView, profile, BBLogoutView, RegisterUserView, RegisterDoneView, create_request, delete_request, request_detail

app_name = 'AppDesign'

urlpatterns = [
    path('', index, name='index'),
    path('accounts/login', BBLoginView.as_view(), name='login'),
    path('accounts/logout/', BBLogoutView.as_view(), name='logout'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/register/', RegisterUserView.as_view(), name='register'),
    path('accounts/register/done/', RegisterDoneView.as_view(), name='register_done'),
    path('create-request', create_request, name='create_requests'),
    path('delete-request/', delete_request, name='delete_request'),
    path('request/<int:request_id>/', request_detail, name='request_detail'),
]
