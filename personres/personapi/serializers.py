from rest_framework import serializers, viewsets
from personres.models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'