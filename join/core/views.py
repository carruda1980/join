from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from join.core.forms import UserLocationForm
from join.core.models import UserLocation
from join.core.serializers import UserLocationSerializer


def home(request):
    # Se for um request vazio retorna o form zerado
    if request.method == 'GET':
        form = UserLocationForm()
        return render(request, 'index.html', {'form': form})
    else:
        # Se no request vier o id do marker entende-se que é atualizar, e faz as devidas validações
        marker_id = True if request.POST.get('marker_id') else False
        if marker_id:
            location = get_object_or_404(UserLocation, pk=request.POST.get('marker_id'))
            form = UserLocationForm(request.POST, instance=location)
            if form.is_valid():
                form.save()
                return redirect('home')
            else:
                return render(request, 'index.html', {'form': form})

        # Caso contrario apenas salva ou retorna erro o form com seus respectivos valores
        else:
            form = UserLocationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
            else:
                return render(request, 'index.html', {'form': form})


def delete(request):
    user_location = get_object_or_404(UserLocation, pk=int(request.POST.get('marker_id')))
    user_location.delete()
    return redirect('home')


class Locations(APIView):
    def get(self, request, format=None):
        if request.GET.get('id'):
            locations = UserLocation.objects.filter(pk=request.GET.get('id'))
            serializer = UserLocationSerializer(locations, many=True)
            return Response(serializer.data)
        else:
            locations = UserLocation.objects.all()
            serializer = UserLocationSerializer(locations, many=True)
            return Response(serializer.data)