from .models import Hopitals
from  rest_framework import serializers

class hospitalsSerializers(serializers.ModelSerializer):
    class Meta:
        model=Hopitals
        fields=(
            'id',
            'name',
            'sulg',
            'urgence',
            'localisation',
            'description',
            'image',
            'date_ajout',
            'get_google_Map_Cordonnee',
    )