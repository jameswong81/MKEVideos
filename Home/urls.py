from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path('test/', views.test_view, name='test_view'),
    path('upload_video/', views.upload_file, name='upload_video'),
]