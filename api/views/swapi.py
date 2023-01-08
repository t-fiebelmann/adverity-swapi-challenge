from rest_framework import status, viewsets
from rest_framework.response import Response
from api.swapi.people import People
from api.models.collection_meta_data import CollectionMetaData
from api.serializers.collection_meta_data import CollectionMetaDataSerializer


class SwapiViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for interfacing with swapi data
    """
    queryset = CollectionMetaData.objects.all()
    serializer_class = CollectionMetaDataSerializer
    people = People()

    def list(self, request):
        return self.queryset

    def create(self, request):
        # this will fetch the latest dataset from swapi
        pass