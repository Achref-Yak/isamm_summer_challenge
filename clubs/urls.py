from django.conf.urls import url
from . import views

#importer le view LoginView
from clubs.views import register,login_view,logout_view
urlpatterns = [
    
    url(r'^welcome/',  register, name='register'),
    url(r'^login/',  login_view, name='login'),
    url(r'^logout/',  logout_view, name='logout'),
   	url(r'^profile/(?P<string>[\w\-]+)/$', views.ProfileView, name='profile_by_id'),
    url(r'^profile/$', views.ProfileView, name='profile'),
   	url(r'^profileEdit/', views.ProfileEdit, name='profileEdit'),
    url(r'^club_create/', views.club_create_view, name='create_club'),
    url(r'^club/(?P<string>[\w\-]+)/$', views.club_view, name='view_club_with_pk'),

]