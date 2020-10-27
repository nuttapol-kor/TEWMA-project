"""Urls for Django appointment app."""
from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'appointment'
urlpatterns = [
    path('', views.IndexView.as_view(), name="home_page"),
    path("meeting/<int:year>/<int:month>/<int:day>", views.meeting_list, name="meet_list"),
    path("<int:meeting_id>/detail", views.detail, name="detail"),
    url(r'result/$', views.search, name="search"),
]
