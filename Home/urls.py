from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path('test/', views.test_view, name='test_view'),
]