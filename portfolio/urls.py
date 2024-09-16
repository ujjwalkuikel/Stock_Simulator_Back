from django.urls import path
from .views import get_portfolio_by_user

urlpatterns = [
    path('portfolio/<int:uid>/', get_portfolio_by_user, name='get_portfolio_by_user'),
]
