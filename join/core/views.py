from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView

from join.core.forms import UserLocationForm
from join.core.models import UserLocation
from join.core.serializers import UserLocationSerializer


def home(request):
    if request.method == 'GET':
        form = UserLocationForm()
        return render(request, 'index.html', {'form': form})
    else:
        form = UserLocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'index.html', {'form': form})


class Locations(APIView):
    def get(self, request, format=None):
        snippets = UserLocation.objects.all()
        serializer = UserLocationSerializer(snippets, many=True)
        return Response(serializer.data)