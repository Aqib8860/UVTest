from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, permissions, generics
from django.core.exceptions import ObjectDoesNotExist
from apis.models import *
from apis.serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


# Create your views here.


class AddDataViewSet(viewsets.ModelViewSet):
	queryset = Country.objects.all()
	serializer_class = AddDataSerializer
	http_method_names = ['post']

	def create(self, request, *args, **kwargs):
		data_type = request.data['data_type']
		# STATE
		if data_type == "State":
			res = State.objects.create(
				data_type=data_type, main_location=request.data['main_location'],
				capital=request.data['capital']
			)
			language = Language.objects.create(name=request.data['language'])
			Population.objects.create(state=res, language=language, population=request.data['population'])
			return Response({"msg": "Data Add Success !!"}, status=200)		

		# CITY
		elif data_type == "City":
			res = City.objects.create(
				data_type=data_type, main_location=request.data['main_location'],
				capital=request.data['capital']
			)
			language = Language.objects.create(name=request.data['language'])
			Population.objects.create(city=res, language=language, population=request.data['population'])
			return Response({"msg": "Data Add Success !!"}, status=200)		
		
		# COUNTRY
		elif data_type == "Country":
			res = Country.objects.create(
				data_type=data_type, main_location=request.data['main_location'],
				capital=request.data['capital']
			)
			language = Language.objects.create(name=request.data['language'])
			Population.objects.create(country=res, language=language, population=request.data['population'])
			return Response({"msg": "Data Add Success !!"}, status=200)		
		else:
			return Response({"msg": "No Data Type Found !!"}, status=400)		


class PopulationDataViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Population.objects.all()
	serializer_class = PopulationSerializer
	filter_backends = [DjangoFilterBackend, filters.SearchFilter]
	"""search_fields = [
		'country__main_location', 'country__data_type', 'country__capital',
		'city__main_location', 'city__data_type', 'city__capital',
		'state__main_location', 'state__data_type', 'state__capital',

	]"""
	filterset_fields = [
		'population','language__name', 
		'country__main_location', 'country__data_type', 'country__capital',
		'city__main_location', 'city__data_type', 'city__capital',
		'state__main_location', 'state__data_type', 'state__capital',		

	]

