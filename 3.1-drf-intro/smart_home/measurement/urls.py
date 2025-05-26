from django.urls import path
from .views import (
    SensorCreateView,
    SensorRetrieveUpdateView,
    SensorListView,
    MeasurementCreateView,
    SensorDetailListView,
)

urlpatterns = [
    path('sensors/', SensorListView.as_view(),
         name='sensor-list'),
    path('sensors/create/', SensorCreateView.as_view(),
         name='sensor-create'),
    path('sensors/<int:pk>/update/', SensorRetrieveUpdateView.as_view(),
         name='sensor-update'),
    path('measurements/create/', MeasurementCreateView.as_view(),
         name='measurement-create'),
    path('sensors/<int:pk>/detail/', SensorDetailListView.as_view(),
         name='sensor-detail'),
]