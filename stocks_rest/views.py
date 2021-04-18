from django.shortcuts import render

from django.http import request, JsonResponse, Http404
from .models import SP500
from .models import DJ30
from .models import Div
from .models import Index
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import SP500Serializer
from .serializer import DJ30Serializer
from .serializer import DivSerializer
from .serializer import IndexSerializer


class ListSP500(APIView):
    def get(self,request):
        obj = SP500.objects.all().order_by("-momentum_12_2")
        serializer_obj = SP500Serializer(obj,many=True)
        return Response(serializer_obj.data)

    def post(self,request):
        data = request.data
        serializer_obj = SP500Serializer(data=data)
        if serializer_obj.is_valid():
            serializer_obj.save()
            return Response(serializer_obj.data)
        return Response(serializer_obj.errors)


class ListDJ30(APIView):
    def get(self,request):
        obj = DJ30.objects.all().order_by("-momentum_12_2")
        serializer_obj = DJ30Serializer(obj,many=True)
        return Response(serializer_obj.data)

    def post(self,request):
        data = request.data
        serializer_obj = DJ30Serializer(data=data)
        if serializer_obj.is_valid():
            serializer_obj.save()
            return Response(serializer_obj.data)
        return Response(serializer_obj.errors)


class ListIndex(APIView):
    def get(self,request):
        obj = Index.objects.all()
        serializer_obj = IndexSerializer(obj,many=True)
        return Response(serializer_obj.data)


    def post(self,request):
        data = request.data
        serializer_obj = IndexSerializer(data=data)
        if serializer_obj.is_valid():
            serializer_obj.save()
            return Response(serializer_obj.data)
        return Response(serializer_obj.errors)


class ListDiv(APIView):
    def get(self,request):
        obj = Div.objects.all().order_by("-p_div")
        serializer_obj = DivSerializer(obj,many=True)
        return Response(serializer_obj.data)

    def post(self,request):
        data = request.data
        serializer_obj = DivSerializer(data=data)
        if serializer_obj.is_valid():
            serializer_obj.save()
            return Response(serializer_obj.data)
        return Response(serializer_obj.errors)
