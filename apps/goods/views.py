from django.shortcuts import render

# Create your views here.

from .serializers import GoodsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Goods

class GoodsListView(APIView):
    """
    List all Goods.
    """
    def get(self, request, format=None):
        snippets = Goods.objects.all()
        serializer = GoodsSerializer(snippets, many=True)
        return Response(serializer.data)
