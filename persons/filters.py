from django_filters import BaseCSVFilter, CharFilter, NumberFilter, rest_framework
from persons.models import Person


class PersonFilter(rest_framework.FilterSet):
    class Meta:
        model = Person
        fields = (
            "document", "names", "last_names", "document_type"
        )
