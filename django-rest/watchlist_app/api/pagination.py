from rest_framework.pagination import PageNumberPagination

class WatchListPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'size'
    max_page_size = 50