# from rest_framework.filters import SearchFilter, OrderingFilter
# from rest_framework.pagination import PageNumberPagination
# from rest_framework.viewsets import ModelViewSet
# from api.views import Category
# from api.serializers import CategorySerializer
#
# class CategoryPagination(PageNumberPagination):
#     page_size = 10  # Number of items per page
#     page_size_query_param = 'page_size'
#     max_page_size = 100
#
# class CategoryViewSet(ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     filter_backends = [SearchFilter, OrderingFilter]
#     search_fields = ['name']
#     ordering_fields = ['name']
#     pagination_class = CategoryPagination


from collections import OrderedDict

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = "limit"
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('total_pages', self.page.paginator.num_pages),
            ('results', data)
        ]))