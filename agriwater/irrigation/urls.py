from django.urls import path
from .views import dashboard, analytics, add_sensor_data

urlpatterns = [
    path("dashboard/", dashboard, name="dashboard"),
    path("analytics/", analytics, name="analytics"),
    path("add-data/", add_sensor_data, name="add_data"),
]
