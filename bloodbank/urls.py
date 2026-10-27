
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    path('donors/', views.donors, name='donors'),
    path('donors/add/', views.donor_add, name='donor_add'),

    path('components/', views.components, name='components'),
    path('components/add/', views.component_add, name='component_add'),

    path('storage/', views.storage, name='storage'),
    path('storage/add/', views.storage_add, name='storage_add'),

    path('dispatches/', views.dispatches, name='dispatches'),
    path('dispatches/add/', views.dispatch_add, name='dispatch_add'),
]

