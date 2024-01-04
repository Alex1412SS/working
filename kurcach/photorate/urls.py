from django.urls import path
from . import views


urlpatterns = [
    path('photos/', views.photo_rate, name='photo_rate'),
    path('create/', views.create, name='create'),
    path('rating/', views.RatingCreateView.as_view(), name='rating'),
]