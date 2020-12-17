from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from join.core.models import UserLocation
from join.core.serializers import UserLocationSerializer


def home(request):
    return render(request, 'index.html')


class Location(APIView):
    def get(self, request, format=None):
        snippets = UserLocation.objects.all()
        serializer = UserLocationSerializer(snippets, many=True)
        return Response(serializer.data)