from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
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

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)

class blogDetailView(DetailView):
    model = BlogModel
    template_name = "pages/blogdetail.html"

class updateView(UpdateView):
    form_class = BlogModelForm
    model = BlogModel
    template_name = "pages/updateactive.html"

    def get_success_url(self):
        return reverse_lazy('main:blogDetailView', kwargs={'pk': self.object.pk})
    
def deleteBlogView(request, pk):
    blog = get_object_or_404(BlogModel, pk=pk)
    if request.method == 'POST':
        blog.delete() 
        return redirect('main:BlogsView')
    return render(request, 'pages/deleteblog.html', {'blog': blog})
