from rest_framework import serializers
from .models import Musician


class MusicianSerializer(serializers.ModelSerializer):
    is_adult = serializers.ReadOnlyField(read_only=True)

    class Meta:
        model = Musician
        fields = [
            "id",
            "first_name",
            "last_name",
            "instrument",
            "age",
            "date_of_applying",
            "is_adult",
        ]

    def validate(self, data):
        musician = Musician(**data)
        musician.clean()
        return data
