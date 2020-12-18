from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from join.core.forms import UserLocationForm
from join.core.models import UserLocation
from join.core.serializers import UserLocationSerializer


def home(request):
    form = UserLocationForm()
    return render(request, 'index.html', {'form': form})


class Locations(APIView):
    def get(self, request, format=None):
        snippets = UserLocation.objects.all()
        serializer = UserLocationSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        print('teste')