from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
from django.core.mail import send_mail
from django.urls import reverse
from .models import Post, User, Response
from .forms import PostCreateForm, ResponseCreateForm

class PostList(generic.ListView):
    model = Post
    ordering = '-created'
    template_name = 'post_list.html'
    context_object_name = 'post_list'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


class PostCreate(LoginRequiredMixin, generic.CreateView):
    model = Post
    template_name = 'post_edit.html'
    form_class = PostCreateForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = User.objects.get(id=self.request.user.id)
        self.object.save()
        result = super().form_valid(form)
        return result


class PostUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Post
    template_name = 'post_edit.html'
    form_class = PostCreateForm

class ResponseCreate(LoginRequiredMixin, generic.CreateView):
    model = Response
    template_name = 'response.html'
    form_class = ResponseCreateForm
    success_url = '/success/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = User.objects.get(id=self.request.user.id)
        self.object.post = Post.objects.get(id=self.kwargs['pk'])
        self.object.save()
        result = super().form_valid(form)
        return result

class ResponseList(LoginRequiredMixin, generic.ListView):
    model = Response
    template_name = 'response_list.html'
    context_object_name = 'response_list'

@login_required()
def response_accept(request, pk):
    response = Response.objects.get(pk=pk)
    response.accept = 'Y'
    response.save()
    send_mail(
        subject=f'Отлик принят.',
        message=f'Ваш отклик на пост "{response.post.title}" принят',
        from_email='rawil-m@yandex.ru',
        recipient_list=[response.user.email]
    )
    return HttpResponseRedirect(reverse('response_list'))

@login_required()
def response_not_accept(request, pk):
    response = Response.objects.get(pk=pk)
    response.accept = 'N'
    response.save()
    return HttpResponseRedirect(reverse('response_list'))

class SuccessView(generic.TemplateView):
    template_name = 'success.html'