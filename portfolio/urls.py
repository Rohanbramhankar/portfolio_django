from django.urls import path

from portfolio import views

urlpatterns = [
    path("", views.home, name="home"),
    path("health/", views.health_check, name="health_check"),
    path("assistant/chat/", views.assistant_chat, name="assistant_chat"),
    path("contact/", views.contact, name="contact"),
    path("python-projects/", views.python_projects, name="python_projects"),
    path("data-analytics-projects/", views.data_analytics_projects, name="data_analytics_projects"),
    path("dotnet-projects/", views.dotnet_projects, name="dotnet_projects"),
]
