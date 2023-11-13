from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from .models import UserModel, BlogModel, BlogCategoryModel, FunctionsModel
from .forms import AccountForm, BlogModelForm, BlogCategoryModelForm
from django.contrib.auth import login, logout, authenticate
from django.core.exceptions import PermissionDenied

class index(ListView):
    model = FunctionsModel
    template_name = "pages/index.html"

class functionsView(DetailView):
    model = FunctionsModel
    template_name = "pages/change.html"
    
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['blogs'] = BlogModel.objects.all()
        return data

class BlogsView(ListView):
    model = BlogModel
    template_name = "pages/blogs.html"

class BlogCreate(CreateView):
    form_class = BlogModelForm
    model = BlogModel
    template_name = "pages/blogcreate.html"
    success_url = reverse_lazy('main:BlogsView')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionDenied("You don't have permission to access this page.")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)
    
class BlogCategoryCreate(CreateView):
    form_class = BlogCategoryModelForm
    model = BlogCategoryModel
    template_name = "pages/blogcategorycreate.html"
    success_url = reverse_lazy('main:BlogCreate')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionDenied("You don't have permission to access this page.")
        return super().dispatch(request, *args, **kwargs)

class blogDetailView(DetailView):
    model = BlogModel
    template_name = "pages/blogdetail.html"

class updateView(UpdateView):
    form_class = BlogModelForm
    model = BlogModel
    template_name = "pages/updateactive.html"

    def get(self, request, *args, **kwargs):
        blog = self.get_object()
        if request.user != blog.user:
            raise PermissionDenied
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('main:blogDetailView', kwargs={'pk': self.object.pk})
    
def deleteBlogView(request, pk):
    blog = get_object_or_404(BlogModel, pk=pk)
    if request.user == blog.user and request.method == 'POST':
        blog.delete() 
        return redirect('main:BlogsView')
    return render(request, 'pages/deleteblog.html', {'blog': blog})
