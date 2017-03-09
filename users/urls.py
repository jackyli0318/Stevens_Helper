from django.conf.urls import url
from .views import register, login, logout


urlpatterns = [
    url(r'^register$', register),
    url(r'^login', login),
    url(r'^logout', logout),
]
