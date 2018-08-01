from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import *

# Create your views here.
class IndexView(ListView):
    template_name = 'article/index.html'
    context_object_name = 'posts'
    # display blank form
    def get_queryset(self):
        return Post.objects.all()

class PostDetail(DetailView):
    model = Post
    template_name = 'article/postdetail.html'