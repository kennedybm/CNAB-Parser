from ...models import Type
from django.core.management import base

class Command(base.BaseCommand):
    help = "Types Generator"

    def handle(self, *args, **kwargs):
        Type.objects.create(description='Débito', nature_choices='Entrada', sinal_choices='+')
        Type.objects.create(description='Boleto', nature_choices='Saída', sinal_choices='-')
        Type.objects.create(description='Financiamento', nature_choices='Saída', sinal_choices='-')
        Type.objects.create(description='Crédito', nature_choices='Entrada', sinal_choices='+')
        Type.objects.create(description='Recebimento Empréstimo', nature_choices='Entrada', sinal_choices='+')
        Type.objects.create(description='Vendas', nature_choices='Entrada', sinal_choices='+')
        Type.objects.create(description='Recebimento TED', nature_choices='Entrada', sinal_choices='+')
        Type.objects.create(description='Recebimento DOC', nature_choices='Entrada', sinal_choices='+')
        Type.objects.create(description='Aluguel', nature_choices='Saída', sinal_choices='-')

        return "Success"