from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_blogs, name='blogs_home'),
    path('<int:blog_id>/', views.details, name='details'),
]