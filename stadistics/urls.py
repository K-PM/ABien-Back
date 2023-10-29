from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.save_water_sample),
    path('get_sample_day/<str:date>', views.get_sample_by_day),
    path('get_model_profile/', views.get_model_profile)
]