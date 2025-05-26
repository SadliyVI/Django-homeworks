from django.db.models import Prefetch
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, \
    ListAPIView
from .models import Sensor, Measurement
from .serializers import (SensorSerializer, MeasurementSerializer,
                          SensorDetailSerializer)



class SensorCreateView(CreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class SensorRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class SensorListView(ListAPIView):
    queryset = Sensor.objects.all().order_by('-id')
    serializer_class = SensorSerializer

class MeasurementCreateView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def perform_create(self, serializer):
        serializer.save()

class SensorDetailListView(ListAPIView):
    serializer_class = SensorDetailSerializer
    def get_queryset(self):
        sensor_id = self.kwargs.get('pk')
        prefetch = Prefetch('measurements',
                            queryset=Measurement.objects.order_by('measured_at'))
        return Sensor.objects.filter(pk=sensor_id).prefetch_related(prefetch)
