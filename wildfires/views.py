from django.shortcuts import render
from django.views import View
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from wildfires.wildfirescript import get_wildfire

# Create your views here.


class WildfireAPIView(APIView):
    """ this view is used if you want to serve your data over an endpoint"""
    def get(self, request):
        try:
            wildfire_data = get_wildfire()
            return Response(wildfire_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)


class WildfireView(View):
    """ this view is used if you want to use django's generic views"""

    def get(self, request):
        try:
            wildfire_data = get_wildfire()
            template_name = 'wildfires/wildfires.html'
            context = {'wildfires': wildfire_data}
            return render(request, template_name, context)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)
