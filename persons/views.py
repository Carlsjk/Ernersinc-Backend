from django.shortcuts import render
from rest_framework import serializers, status, viewsets
from persons.models import Person
from persons.serializers import PersonModelSerializer
from rest_framework.response import Response
import datetime
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from persons.filters import PersonFilter
from persons.utils.pagination import StandardResultsSetPagination
# Create your views here.


class PersonViewSet(viewsets.ModelViewSet):
    queryset = (
        Person.objects.filter(deleted_at=None)
    )
    serializer_class = PersonModelSerializer
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    pagination_class = StandardResultsSetPagination
    page_size = 5
    page_size_query_param = "page_size"
    max_page_size = 20
    ordering_fields = ["created_at", "updated_at"]
    search_fields = ["document", "names", "last_names", "document_type"]
    filterset_class = PersonFilter

    def get_serializer_class(self):
        return PersonModelSerializer
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.deleted_at = datetime.datetime.now()
        count_document = (
            Person.objects.filter(document__icontains=instance.document + "_deleted").values("document").count()
        )
        instance.document = instance.document + "_deleted" + f"{count_document + 1}"
        instance.save()
        return Response(
            {"mensaje": "Eliminado correctamente"}, 
            status=status.HTTP_200_OK
        )