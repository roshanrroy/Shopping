from rest_framework import serializers
from Location.models import StatesModel,CityModel
 
class StateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StatesModel
        fields = ('state_id', 'statename')


class CitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CityModel
        fields = ('city_id','cityname','state_id')