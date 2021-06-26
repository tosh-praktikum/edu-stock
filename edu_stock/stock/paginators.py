from rest_framework import pagination

class OrderPaginator (pagination.CursorPagination):
    ordering = 'id'
    page_size = 1