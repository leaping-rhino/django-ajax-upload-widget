from django.conf.urls import url

from ajax_upload.urls import urlpatterns


urlpatterns += [
    url(r'^test/$', 'ajax_upload.tests.views.test_view', name='ajax-uploads-test'),
]
