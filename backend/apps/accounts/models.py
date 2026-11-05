from django.conf import settings
from django.db import models
from django.core.validators import MinValueValidator

class Account(models.Model):
    class AccountType(models.TextChoices):
        CASH = "CASH", "Cash"
        BANK = "BANK", "Bank"
        SAVINGS = "SAVINGS", "Savings"
        CREDIT = "CREDIT", "Credit"
        OTHER = "OTHER", "Other"

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="finance_accounts")
    name = models.CharField(max_length=80)
    account_type = models.CharField(max_length=12, choices=AccountType.choices, default=AccountType.BANK)
    currency = models.CharField(max_length=3, default="AED")
    opening_balance = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    is_archived = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]
        constraints = [
            models.UniqueConstraint(fields=["user", "name"], name="uniq_account_name_per_user"),
        ]

    def __str__(self):
        return f"{self.name} ({self.currency})"
