from django.conf.urls import url
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^inbox/$', get_inbox_index, name='inbox'),
    url(r'^sent/$', get_sent_index, name='sent'),
    url(r'^message/(\d+)$', get_mail_index, name='view_message'),
    url(r'compose_message/$', get_compose_index, name='compose_message'),
]
