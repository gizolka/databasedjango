from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test/<int:test_1>/', views.test, name='test'),
    path('', views.login, name='login'),
    ]
