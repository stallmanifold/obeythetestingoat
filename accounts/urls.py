from django.conf.urls import include, url
from accounts import views as account_views


urlpatterns = [
    url(r'^send_login_email$', account_views.send_login_email, name='send_login_email'),
    url(r'^login$', account_views.login, name='login'),
]
