from rest_framework import serializers
from .models import *
from django.core.exceptions import ObjectDoesNotExist


class AddDataSerializer(serializers.ModelSerializer):
	population = serializers.CharField(max_length=20, write_only=True)
	language = serializers.CharField(max_length=30, write_only=True)

	class Meta:
		model = Country
		fields = ['data_type', 'main_location', 'capital', 'population', 'language']


class PopulationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Population
		fields = '__all__'
		depth = 2


class LanguageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Language
		fields = ['name']


