from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from .forms import RegisterUserForm, InteriorDesignRequestForm
from .models import AdvUser, InteriorDesignRequest
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.contrib import messages
from django.shortcuts import get_object_or_404



def index(request):
    requests = InteriorDesignRequest.objects.all()
    return render(request, 'catalog/index.html', {'requests': requests})

class BBLoginView(LoginView):
    template_name = 'catalog/login.html'
    def form_valid(self, form):
        user=form.get_user()
        user.status='online'
        user.save()
        return super().form_valid(form)

class BBLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'catalog/logout.html'

@login_required
def profile(request):
    user_requests = InteriorDesignRequest.objects.filter(user=request.user)
    return render(request, 'catalog/profile.html', {'user_requests': user_requests})

class RegisterUserView(CreateView):
    model = AdvUser
    template_name = 'catalog/register_user.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('catalog:register_done')

class RegisterDoneView(TemplateView):
    template_name = 'catalog/register_done.html'


def create_request(request):
    if request.user.is_staff:
        messages.error(request, "Администраторы не могут создавать заявки.")
        return redirect('catalog:profile')

    if not request.user.is_active:
        messages.error(request, "Вы не можете создавать заявки до активации.")
        return redirect('catalog:profile')

    if request.method == 'POST':
        form = InteriorDesignRequestForm(request.POST, request.FILES)
        if form.is_valid():
            is_urgent = form.cleaned_data.get('is_urgent', False)
            if is_urgent and InteriorDesignRequest.objects.filter(user=request.user, is_urgent=True).exists():
                messages.error(request, "Вы уже создали срочную заявку.")
                return redirect('catalog:create_requests')
            request_instance = form.save(commit=False)
            request_instance.user = request.user
            request_instance.category = form.cleaned_data['new_category'] or form.cleaned_data['category']
            request_instance.save()
            messages.success(request, 'Ваша заявка успешно отправлена!')
            return redirect('catalog:profile')
    else:
        form = InteriorDesignRequestForm()

    return render(request, 'catalog/create_requests.html', {'form': form})

def delete_request(request):
    user_requests = InteriorDesignRequest.objects.filter(user=request.user)
    if request.user.is_staff:
        messages.error(request, "Администраторы не могут удалять заявки.")
        return redirect('catalog:profile')

    if request.method == 'POST':
        request_id = request.POST.get('request_id')
        request_instance = get_object_or_404(InteriorDesignRequest, id=request_id, user=request.user)
        request_instance.delete()
        messages.success(request, "Заявка успешно удалена.")
        return redirect('catalog:profile')

    return render(request, 'catalog/delete_request.html', {'user_requests': user_requests})