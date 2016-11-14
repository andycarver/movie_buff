from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_actor$', views.add_actor),
    # url(r'^show_actor$', views.show_actor),
    url(r'^add_movie$', views.add_movie),
    # url(r'^update_actor$', views.update_actor),
]
