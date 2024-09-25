from . import views
from django.urls import path

urlpatterns = [
    path('login/', views.login),
    path('signup/', views.signup),
    path('logout/', views.logout),
    path('test/', views.test_token),

]

