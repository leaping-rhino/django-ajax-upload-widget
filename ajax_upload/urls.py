from django.conf.urls import url

from ajax_upload import views

appname = 'ajax_upload'
urlpatterns = [
    url(r'^$', views.upload, name='ajax-upload'),
]
