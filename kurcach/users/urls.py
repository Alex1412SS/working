from django.urls import path
from . import views
from users.views import logout

urlpatterns = [
    path('', views.reg, name='reg'),
    path('login/', views.log, name="log"),
    path('profile/', views.profile, name="profile"),
    path('logout/', logout, name="logout")
]