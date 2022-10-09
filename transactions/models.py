from django.db import models

class Transaction(models.Model):
    class meta:
        ordering = ["-id"]

    date = models.DateTimeField()
    amount = models.FloatField()
    cpf = models.CharField(max_length=11)
    card = models.CharField(max_length=12)
    owner = models.CharField(max_length=14)
    store_name = models.CharField(max_length=19)
    transaction_type = models.ForeignKey("normalizers.Type", on_delete=models.CASCADE, related_name="transactions")



