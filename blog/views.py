from django.views.generic import *
from blog.models import *
from django.urls import reverse_lazy

class BlogLV(ListView):
    model = Post

class blogCV(CreateView):
    model = Post
    fields = ['title', 'description', 'image']
    template_name_suffix = '_create'
    success_url = reverse_lazy('blog')

class blogUV(UpdateView):
    model = Post
    fields = ['title', 'description', 'image', 'id']
    template_name_suffix = '_update'
    success_url = reverse_lazy('blog')

class blogRV(DeleteView):
    model = Post
    success_url = reverse_lazy('blog')