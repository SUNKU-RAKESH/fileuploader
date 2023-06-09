from django.urls import path, include
from . import views

urlpatterns = [
 path('home', views.home, name="home"),
 path('motech/', views.motech, name="motech"),
 path('youtube/', views.youtube, name='youtube'),
 path('form/', views.uploadForm, name='form'),
 path('upload/', views.uploadFile, name='upload'),
 path('files/', views.FileView.as_view(), name='files'),
 path('myupload/', views.myUpload, name='myupload'),

 path('', views.PelconView.as_view(), name='pelcon'),
 path('pelconUpload/', views.pelconUpload, name='pelconUpload'),




]
