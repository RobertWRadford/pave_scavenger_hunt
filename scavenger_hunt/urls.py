from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
	path('', views.home_view, name='home'),
	path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('activate_account_sent/', views.activate_account_sent_view, name='activate_account_sent'),
    path('activate_account_invalid/', views.activate_account_invalid_view, name='activate_account_invalid'),
    path('activate/<slug:uidb64>/<slug:token>/', views.activate_view, name='activate'),
    path('scavengerhunt/<str:loc>', views.scavengerhunt_view, name='scavengerhunt'),
	path('start/<str:loc>', views.start_view, name='start'),
	path('extras/', views.extras_view, name='extras'),
    path('completed/', views.completed_view, name='completed'),
	path('about/', views.about_view, name='about'),
]