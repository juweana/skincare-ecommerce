from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet, OrderCreateView, DashboardCountsView

router = DefaultRouter()
router.register("categories", CategoryViewSet)
router.register("products", ProductViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

urlpatterns = [
    path("", include(router.urls)),
    path("orders/", OrderCreateView.as_view()),
]

urlpatterns = [
    path("", include(router.urls)),
    path("orders/", OrderCreateView.as_view()),
    path("dashboard/counts/", DashboardCountsView.as_view()),
]