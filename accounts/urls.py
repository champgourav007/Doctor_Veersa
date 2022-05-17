from django.urls import path
from . import views

urlpatterns = [
    path("", views.index_view, name="index-page"),
    path('login/', views.login_view, name="login-page"),
    path('signup/', views.signup_view, name="signup-page"),
    path('logout/', views.logout_view, name="logout-page"),
    path('book-appointment/<pk>/<user>', views.book_appointment, name="book-appointment"),
    path('home-page/<pk>', views.home_page, name='home-page'),
    path('profile/<pk>', views.show_profile, name="profile"),
    path('save-appointment/<doctor>/<user>', views.save_appointment, name="save-appointment"),
]
