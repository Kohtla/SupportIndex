from django.conf.urls import url
from . import views

app_name = 'main'

urlpatterns = [
    # /shop/
    url(r'^$', views.IndexView.as_view(), name = 'index'),
    url(r'^portfolio/', views.Portfolio.as_view(), name ='portfolio'),
    url(r'^(?P<pk>[0-9]+)/$', views.SiteDetail.as_view(), name="detail"),
]