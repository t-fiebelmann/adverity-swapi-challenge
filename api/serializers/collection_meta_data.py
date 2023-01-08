from rest_framework import serializers
from api.models.collection_meta_data import CollectionMetaData


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectionMetaData
        fields = ('id', 'filename', 'date_downloaded')
