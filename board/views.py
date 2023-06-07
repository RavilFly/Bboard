from django.views import generic
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


class PostCreate(generic.CreateView):
    model = Post
    template_name = 'post_edit.html'
    form_class = PostCreateForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = User.objects.get(id=self.request.user.id)
        self.object.save()
        result = super().form_valid(form)
        return result


class PostUpdate(generic.UpdateView):
    model = Post
    template_name = 'post_edit.html'
    form_class = PostCreateForm

class ResponseCreate(generic.CreateView):
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

class ResponseList(generic.ListView):
    model = Response
    template_name = 'response_list.html'
    context_object_name = 'response_list'


class SuccessView(generic.TemplateView):
    template_name = 'success.html'