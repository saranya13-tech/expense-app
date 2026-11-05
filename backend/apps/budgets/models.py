from django.conf import settings
from django.db import models

class Budget(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="finance_budgets")
    category = models.ForeignKey("categories.Category", on_delete=models.CASCADE, related_name="budgets")
    month = models.DateField(help_text="Use the first day of the budget month")
    amount = models.DecimalField(max_digits=14, decimal_places=2)
    currency = models.CharField(max_length=3, default="AED")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "category", "month"], name="uniq_budget_user_category_month"),
        ]
