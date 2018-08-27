from django.conf.urls import url
from . import views
from django.views.generic import TemplateView
from .api import ClubApi, ActivityApi, EventApi, DemandeApi, UserApi
from rest_framework.routers import DefaultRouter
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
    url(r'^invitations/$',views.InvitationView,name="invitation"),
    url(r'^invitations/(?P<add>[\w\-]+)/$',views.InvitationView,name="invitation_with_string"),
    url(r'^invitations/del/(?P<delete>[\w\-]+)/$',views.InvitationView,name="invitation_with_string"),
    url(r'^club/(?P<string>[\w\-]+)/$', views.club_view, name='view_club_with_pk'),
    url(r'^event/(?P<string>[\w\-]+)/$', views.event_view, name='view_event_with_pk'),

]

router = DefaultRouter()
router.register(r'demandes', DemandeApi)
router.register(r'activity', ActivityApi)
router.register(r'events', EventApi)
router.register(r'clubs', ClubApi)
router.register(r'users', UserApi)
 
urlpatterns += router.urls