from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'Forum'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^logout$', login_required(views.LogoutRedirectView.as_view()), name='logout'),
]
