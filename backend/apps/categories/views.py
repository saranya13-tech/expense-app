from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Category
from .serializers import CategorySerializer
class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Category.objects.filter(is_active=True).filter(user__isnull=True, is_system=True) | Category.objects.filter(user=self.request.user, is_active=True)
    def perform_create(self, serializer): serializer.save(user=self.request.user, is_system=False)
