from django.urls import path, include 
from rest_framework.routers import DefaultRouter
from profiles_api import views

#routers are used for VIEW-SETS, really cool, will automatically generate the URLs and we can just pass it into our urlpatterns arr
router = DefaultRouter()

router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset') #need to specify base name since there is no queryset.
router.register('profile',views.UserProfileViewSet) #no base name since this is a model viewset

#this is basically a router like nodeJS
urlpatterns = [
    path('hello-view', views.HelloApiView.as_view()),
    path('',include(router.urls))
]