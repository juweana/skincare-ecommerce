from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category, Product, Order, OrderItem
from .serializers import CategorySerializer, ProductSerializer, OrderSerializer


# 1. Define your pagination class first
class StandardResultSetPagination(PageNumberPagination):
    page_size = 12                  # Items per page by default
    page_size_query_param = 'page_size'  # Allows frontend to change it via ?page_size=20
    max_page_size = 48


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all().order_by("name")
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.filter(is_active=True).order_by("-created_at")
    serializer_class = ProductSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ["category"]
    search_fields = ["name"]
    ordering_fields = ["price", "created_at"]
    # 2. Use the exact matching class name here:
    pagination_class = StandardResultSetPagination


class OrderCreateView(generics.CreateAPIView):
    serializer_class = OrderSerializer


class DashboardCountsView(APIView):
    def get(self, request):
        data = {
            "products": Product.objects.count(),
            "active_products": Product.objects.filter(is_active=True).count(),
            "categories": Category.objects.count(),
            "orders": Order.objects.count(),
            "order_items": OrderItem.objects.count(),
        }

        return Response(data)