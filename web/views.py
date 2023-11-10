from django.shortcuts import render, redirect, reverse
from django.utils.translation import gettext as _
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from .models import UserModel
from .forms import AccountForm
from django.contrib.auth import login, logout, authenticate

class index(TemplateView):
    template_name = "pages/index.html"