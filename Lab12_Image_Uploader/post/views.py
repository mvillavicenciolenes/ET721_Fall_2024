from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm

class HomePageView(ListView):
    model = Post
    template_name = 'post/home.html'  # Ensure this matches the path
    context_object_name = 'posts'  # This will be used in the template

class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post/post.html'  # Ensure this matches the path
    success_url = reverse_lazy('home')