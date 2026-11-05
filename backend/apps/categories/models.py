from django.conf import settings
from django.db import models
class Category(models.Model):
    class Kind(models.TextChoices):
        INCOME = "INCOME", "Income"
        EXPENSE = "EXPENSE", "Expense"
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="finance_categories", null=True, blank=True)
    name = models.CharField(max_length=60)
    kind = models.CharField(max_length=8, choices=Kind.choices)
    icon = models.CharField(max_length=40, blank=True)
    color = models.CharField(max_length=12, blank=True)
    is_system = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    class Meta:
        ordering = ["kind", "name"]
        constraints = [models.UniqueConstraint(fields=["user", "name", "kind"], name="uniq_user_category_name_kind")]
    def __str__(self): return f"{self.name} ({self.kind})"
