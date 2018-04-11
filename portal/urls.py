from django.urls import path, re_path

from . import views

app_name = 'portal'
urlpatterns = [
    # ex: /polls/
    re_path(r'^$', views.HomePageView.as_view(), name='home'),
    re_path(r'^about$', views.AboutPageView.as_view(), name='about'),
    re_path(r'^phone/(?P<phonenum>[0-9]+)/$', views.PhoneDetailView.as_view() ,name="detail"),
    # path('phone/<int:pk>/', views.PhoneDetailView.as_view(), name='detail')
    re_path(r'^phone/(?P<phonenum>[0-9]+)/report', views.report, name='report')
]