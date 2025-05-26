from rest_framework import serializers

from .models import Sensor, Measurement
class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ('id', 'name', 'description')

class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ('sensor', 'temperature', 'measured_at')

class MeasurementDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ('temperature', 'measured_at')

class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Sensor
        fields = ('id', 'name', 'description', 'measurements')

