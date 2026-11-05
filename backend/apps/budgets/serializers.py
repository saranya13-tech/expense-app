from rest_framework import serializers
from .models import Budget

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ("id", "category", "month", "amount", "currency", "created_at")
        read_only_fields = ("id", "created_at")
    def validate(self, attrs):
        request = self.context["request"]
        category = attrs.get("category", getattr(self.instance, "category", None))
        if category and category.user_id not in (None, request.user.id):
            raise serializers.ValidationError({"category": "Invalid category."})
        if category and category.kind != "EXPENSE":
            raise serializers.ValidationError({"category": "Budgets can only use expense categories."})
        return attrs
