from django.conf.urls import url

from . import views
app_name='social_network'
urlpatterns = [
    url(r'^home/', views.home, name='home'),
    url(r'^user_login/', views.user_login, name='user_login'),
    url(r'^user_signup/', views.user_signup, name='user_signup'),
    url(r'^signup_auth/', views.signup_auth, name='signup_auth'),
    url(r'^user_wall/', views.user_wall, name='user_wall'),
    url(r'^$', views.user_login, name='user_login'),
    url(r'^user_auth/', views.user_auth, name='user_auth'),
    url(r'^user_logout/', views.user_logout, name='user_logout'),
    url(r'^add_status/', views.add_status, name='add_status'), 
    url(r'^(?P<post_id>[0-9]+)/$', views.add_comment, name='add_comment'),
    url(r'^user/(?P<user_id>[0-9]+)/$', views.show_user, name='show_user'),


]

