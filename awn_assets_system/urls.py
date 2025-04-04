from django.urls import path

from awn_assets_system import views

app_name = "awn_assets_system"

urlpatterns = [
    path('', views.home, name="home"),

]