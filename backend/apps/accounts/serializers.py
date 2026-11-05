from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    balance = serializers.SerializerMethodField()
    class Meta:
        model = Account
        fields = ("id", "name", "account_type", "currency", "opening_balance", "balance", "is_archived", "created_at")
        read_only_fields = ("id", "balance", "created_at")
    def get_balance(self, obj):
        from apps.transactions.services import account_balance
        return str(account_balance(obj))
    def validate_currency(self, value):
        value = value.upper()
        if len(value) != 3:
            raise serializers.ValidationError("Currency must be a 3-letter ISO code.")
        return value
