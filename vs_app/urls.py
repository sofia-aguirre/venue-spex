from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url 

urlpatterns = [
    # landing page
    path('',views.landing, name='landing'),

    # user register and login/logout
    path('signup', views.signup, name='signup'),
    path('login',views.log_in,name='login'),
    path('logout', views.log_out, name='logout'),

    # user views
    path('users', views.user_list, name='user_list'),
    path('users/<int:pk>', views.user_detail, name='user_detail'),
    path('users/<int:pk>/edit', views.user_edit, name='user_edit'),
    path('users/<int:pk>/delete', views.user_delete, name='user_delete'),

    # venue views
    path('venues', views.venue_list, name='venue_list'),
    path('venues/new', views.venue_create, name='venue_create'),
    path('venues/<int:pk>', views.venue_detail, name='venue_detail'),
    path('venues/<int:pk>/edit', views.venue_edit, name='venue_edit'),
    path('venues/<int:pk>/delete', views.venue_delete, name='venue_delete'),
    # venue department views
    path('venues/<int:pk>/sound', views.venue_sound, name='venue_sound'),
    path('venues/<int:pk>/lights', views.venue_lights, name='venue_lights'),
    path('venues/<int:pk>/power', views.venue_electrical, name='venue_electrical'),
    path('venues/<int:pk>/stage', views.venue_stage, name='venue_stage'),
    path('venues/<int:pk>/backstage', views.venue_back, name='venue_back'),

    # comments views
    path('comments', views.comment_list, name='comment_list'),
    path('coments/new', views.comment_create, name='comment_create'),
    path('comments/<int:pk>', views.comment_detail, name='comment_detail'),
    path('comments/<int:pk>/edit', views.comment_edit, name='comment_edit'),
    path('comments/<int:pk>/delete', views.comment_delete, name='comment_delete'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)