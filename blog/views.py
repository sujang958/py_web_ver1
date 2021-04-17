from django.views.generic import *
from blog.models import *

class BlogLV(ListView):
    model = Post