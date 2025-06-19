from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        messages.success(self.request, f'👋 مرحبًا {form.get_user().username}، تم تسجيل الدخول بنجاح!')
        return super().form_valid(form)

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '🎉 تم إنشاء حسابك بنجاح! يمكنك الآن تسجيل الدخول.')
            return redirect(reverse_lazy('accounts:login'))
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})
