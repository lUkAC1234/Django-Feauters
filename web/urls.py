from django.urls import path,include
from .views import index, functionsView, BlogsView, blogDetailView, updateView, \
deleteBlogView, BlogCreate


app_name = "main"

urlpatterns = [
    path('', index.as_view(), name="index"),
    path('function/<int:pk>/', functionsView.as_view(), name="functionsView"),
    path('blogs/list/', BlogsView.as_view(), name="BlogsView"),
    path('blog/detail/<int:pk>/', blogDetailView.as_view(), name="blogDetailView"),
    path('blog/create/', BlogCreate.as_view(), name="BlogCreate"),
    path('update/blog/<int:pk>/', updateView.as_view(), name="updateView"),
    path('delete/blog/<int:pk>/', deleteBlogView, name="deleteBlogView"),
]
