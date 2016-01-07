from views import Landing
from django.conf.urls import url

urlpatterns = [
    url(r'^$', Landing.as_view(), name='landing'),
]
