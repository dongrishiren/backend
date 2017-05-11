from django.conf.urls import url
from django.views.generic import TemplateView

from data import views

urlpatterns = [
    url(r'^back_index$', views.back_index, name="back_index"),
    url(r'^shoes_info$', views.shoes_info, name="shoes_info"),
    url(r'^clothes_info$', views.clothes_info, name="clothes_info"),
    url(r'^tools_info$', views.tools_info, name="tools_info"),
    url(r'^back_register_do$', views.back_register_do, name="back_register_do"),
    url(r'^loginout$', views.loginout, name="loginout"),
    url(r'^login_re$', views.login_re, name="login_re"),
    url(r'^get_backend_info$', views.get_backend_info, name="get_backend_info"),
    url(r'^save_uploadrecord$', views.save_uploadrecord, name="save_uploadrecord"),
    url(r'^get_uploadrecord$', views.get_uploadrecord, name="get_uploadrecord"),
]