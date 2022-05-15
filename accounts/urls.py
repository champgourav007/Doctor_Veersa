from django.urls import path
from . import views

urlpatterns = [
    path("", views.index_view, name="index-page"),
    path('login/', views.login_view, name="login-page"),
    path('signup/', views.signup_view, name="signup-page"),
    path('logout/', views.logout_view, name="logout-page"),
]
