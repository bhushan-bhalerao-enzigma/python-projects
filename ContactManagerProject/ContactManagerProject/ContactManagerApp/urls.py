from django.conf.urls import url

from . import views

app_name = 'ContactManagerApp'
urlpatterns = [
    url(r'^$', views.ContactList, name='contactList'),
    url(r'^modify_contact/(?P<id>[0-9]+)', views.modify_contact, name='modify_contact'),
    url(r'^insert_contact/$', views.insert_contact, name='insert_contact'),
    url(r'^delete_contact/(?P<id>[0-9]+)', views.delete_contact, name='delete_contact'),
]