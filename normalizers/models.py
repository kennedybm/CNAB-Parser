from django.db import models

class SinalChoices(models.TextChoices):
    ADD = "+"
    SUBTRACT = "-"

class TransactionsChoices(models.TextChoices):
    ADD = "Entrada"
    SUBTRACT = "Saida"

class Type(models.Model):
    class meta:
        ordering = ["-int"]

    int = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=100)
    nature_choices = models.CharField(max_length=20, choices=TransactionsChoices.choices)
    sinal_choices = models.CharField(max_length=20, choices=SinalChoices.choices)



