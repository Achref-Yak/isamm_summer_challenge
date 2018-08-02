from django.conf.urls import url
from . import views

#importer le view LoginView
from clubs.views import LoginView
urlpatterns = [
    
    url(r'^login/', LoginView.as_view(), name='login'),
   	url(r'^profile/', views.ProfileView, name='profile'),


]