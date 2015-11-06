from django.conf.urls import include, url
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^accounts/loginuser/$', 'user.views.login'),
    url(r'^accounts/auth/', 'user.views.auth_view'),
    url(r'^accounts/logout/', 'user.views.logout_view'),
    url(r'^accounts/loggedin/$', 'user.views.loggedin'),
    url(r'^accounts/invalid/$', 'user.views.invalid_login'),
    url(r'^register', 'user.views.register_user', name="register"),
    url(r'^login$', 'user.views.render_login', name="login"),



]



