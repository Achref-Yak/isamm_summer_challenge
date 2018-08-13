from django.conf.urls import url
from . import views

#importer le view LoginView
from clubs.views import register,login_view,logout_view
urlpatterns = [
    
    url(r'^welcome/',  register, name='register'),
    url(r'^login/',  login_view, name='login'),
    url(r'^logout/',  logout_view, name='logout'),
   	url(r'^profile/', views.ProfileView, name='profile'),
   	url(r'^profileEdit/', views.ProfileEdit, name='profileEdit'),


]