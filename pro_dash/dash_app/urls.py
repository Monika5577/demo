from django.conf.urls import include , url
from dash_app.views import *
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

app_name = 'dash_app'

urlpatterns = [

    url(r'^signup/$', signup, name='signup'),
    url(r'^signup/login/$', auth_views.login, {'template_name': 'dash_app/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^login/KPIs_dashboard/$', home, name='home'),
    url(r'^profile/', TemplateView.as_view(template_name='profile.html')),
    url(r'^saved/', SaveProfile , name='SaveProfile'),
]

