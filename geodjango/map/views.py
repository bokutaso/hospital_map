from rest_framework import viewsets
from rest_framework_gis.filters import DistanceToPointFilter, InBBoxFilter
from rest_framework.pagination import PageNumberPagination
from .serializers import BorderSerializer
from .models import Border

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import traceback
import json
from django.core.serializers import serialize
from django.shortcuts import render


def index(request):
    contexts = {}
    return render(request,'map/index.html',contexts)

class GeojsonAPIView(APIView):
    def get(self, request, *args, **keywords):
        try:
            encjson  = serialize('geojson', Border.objects.filter(n03_004="中央区"),srid=4326, geometry_field='geom', fields=('n03_003','n03_004',) )
            result   = json.loads(encjson)
            response = Response(result, status=status.HTTP_200_OK)
        except Exception as e:
            traceback.print_exc()
            response = Response({}, status=status.HTTP_404_NOT_FOUND)
        except:
            response = Response({}, status=status.HTTP_404_NOT_FOUND)

        return response

