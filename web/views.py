from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from .models import UserModel, BlogModel, FunctionsModel
from .forms import AccountForm, BlogModelForm
from django.contrib.auth import login, logout, authenticate

class index(ListView):
    model = FunctionsModel
    template_name = "pages/index.html"

class functionsView(DetailView):
    model = FunctionsModel
    template_name = "pages/change.html"
    extra_context = {
        'blogs': BlogModel.objects.all()
    }

class blogDetailView(DetailView):
    model = BlogModel
    template_name = "pages/blogdetail.html"

class updateView(UpdateView):
    form_class = BlogModelForm
    model = BlogModel
    template_name = "pages/updateactive.html"

    def get_success_url(self):
        return reverse_lazy('main:index')