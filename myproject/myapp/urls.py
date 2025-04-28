from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='boat'),
    path('boat/<slug:slug>/', views.boat, name='boat'),
    path('package/<slug:slug>/', views.package, name='package'),
    path('property/', views.property, name='property')
]