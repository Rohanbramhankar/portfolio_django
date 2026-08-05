from django.urls import path
from .views import home, contact


from portfolio import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('python-projects/', views.python_projects, name='python_projects'),
    path('contact/', contact, name='contact'),
   path(
    'data-analytics-projects/',
    views.data_analytics_projects,
    name='data_analytics_projects'
    ),
    path(
    'dotnet-projects/',
    views.dotnet_projects,
    name='dotnet_projects'
),
    
]

