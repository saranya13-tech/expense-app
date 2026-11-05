from rest_framework import serializers
from .models import Category
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name", "kind", "icon", "color", "is_system", "is_active")
        read_only_fields = ("id", "is_system")
