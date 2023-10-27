from django.urls import path
from .import views
urlpatterns = [
    path("",views.index, name = 'index'),
    path("home",views.home, name = 'home'),
    path("profile",views.profile,name = 'profile'),
    path('logout',views.signout,name='logout'),
    path("register",views.signup,name='register'),
    path('addpost',views.addPost,name='addpost')
]