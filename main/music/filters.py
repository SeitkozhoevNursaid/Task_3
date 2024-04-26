from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


class CustomSearchFilter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        if request.query_params.get('name'):
            return ['name']
        return super().get_search_fields(view, request)


