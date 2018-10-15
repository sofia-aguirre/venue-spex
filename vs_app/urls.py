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
    # path('venues/<int:pk>/edit', views.venue_edit, name='venue_edit'),
    path('venues/<int:pk>/delete', views.venue_delete, name='venue_delete'),
    


    # path('api/users', views.sendJson, name='sendJson'),
    # path('special',views.special, name='special'),



]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)