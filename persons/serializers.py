from rest_framework import serializers
from persons.models import Person


class PersonModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        exclude = ["deleted_at"]
