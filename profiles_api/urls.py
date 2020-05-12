from django.urls import path
from profiles_api import views

#this is basically a router like nodeJS
urlpatterns = [
    path('hello-view', views.HelloApiView.as_view()),
]