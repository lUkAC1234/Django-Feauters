from django.urls import path,include
from .views import index, functionsView, blogDetailView, updateView


app_name = "main"

urlpatterns = [
    path('', index.as_view(), name="index"),
    path('function/<int:pk>', functionsView.as_view(), name="functionsView"),
    path('blog/detail/<int:pk>', blogDetailView.as_view(), name="blogDetailView"),
    path('update/<int:pk>/', updateView.as_view(), name="updateView"),
]
