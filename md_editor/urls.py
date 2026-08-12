from django.urls import path
from . import views

urlpatterns = [
    path('api/upload/', views.upload_view, name="upload_view")
]
