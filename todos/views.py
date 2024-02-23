from django.shortcuts import render
from django.views import generic

from todos.models import Todos


# Create your views here.
class IndexView(generic.ListView):
    template_name = "todos/index.html"

    def get_queryset(self):
        return Todos.objects.all()
