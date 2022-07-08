from django.urls import path

from home import views

urlpatterns = [
    path('', views.home, name="home"),
    path('contact', views.contact, name="contact"),
    path('about', views.about, name="about"),
    path('resumebuilder', views.resumebuilder, name="resumebuilder"),
    path('signup', views.handleSignUp, name="handleSignUp"),
    path('login', views.handelLogin, name="handleLogin"),
    path('logout', views.handelLogout, name="handleLogout"),
]
