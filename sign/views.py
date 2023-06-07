# from django.contrib.auth.models import User
# from django.views.generic.edit import CreateView
# from .models import BaseRegisterForm
#
#
# class BaseRegisterView(CreateView):
#     model = User
#     form_class = BaseRegisterForm
#     success_url = '/'

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from string import hexdigits
from django.core.mail import send_mail
import random

from .forms import BaseRegisterForm
from .models import OneTimeCode

class BaseRegisterView(CreateView):
    model = User
    template_name = 'sign/signup.html'
    form_class = BaseRegisterForm
    #success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BaseRegisterForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
        return redirect('code', request.POST['username'])

class GetCode(CreateView):
    template_name = 'sign/code.html'

    def get_context_data(self, **kwargs):
        name_user = self.kwargs.get('user')
        if not OneTimeCode.objects.filter(user=name_user).exists():
            code = random.randint(1000, 9999)
            OneTimeCode.objects.create(user=name_user, code=code)
            user = User.objects.get(username=name_user)
            send_mail(
                subject=f'Код активации',
                message=f'Код активации аккаунта: {code}',
                from_email='rawil-m@ya.ru',
                recipient_list=[user.email]
            )

    def post(self, request, *args, **kwargs):
        if 'code' in request.POST:
            user = request.path.split('/')[-1]
            if OneTimeCode.objects.filter(code=request.POST['code'], user=user).exists():
                User.objects.filter(username=user).update(is_active=True)
                OneTimeCode.objects.filter(code=request.POST['code'], user=user).delete()
            else:
                return render(self.request, 'sign/invalid_code.html')
        return redirect ('login')