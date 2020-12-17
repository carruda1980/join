from rest_framework import serializers

from join.core.models import UserLocation


class UserLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLocation
        fields = ['nome', 'latitude', 'longitude']
