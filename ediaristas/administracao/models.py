from django.db import models

class Servico(models.Model):
    ICONE_CHOICES = [
        ('twf-cleaning-1','twf-cleaning-1'),
        ('twf-cleaning-2', 'twf-cleaning-2'),
        ('twf-cleaning-3', 'twf-cleaning-3'),
    ]
    nome = models.CharField(max_length=50, null=False, blank=False)
    valor_minimo = models.DecimalField(decimal_places=2, max_digits=5,
                                       null=False, blank=False)
    qtd_horas = models.IntegerField(null=False, blank=False)
    porcentagem_comissao = models.DecimalField(decimal_places=2, max_digits=5,
                                               null=False, blank=False)
    horas_quarto = models.IntegerField(null=False, blank=False)
    valor_quarto = models.DecimalField(decimal_places=2, max_digits=5,
                                       null=False, blank=False)
    horas_sala = models.IntegerField(null=False, blank=False)
    valor_sala = models.DecimalField(decimal_places=2, max_digits=5,
                                     null=False, blank=False)
    horas_banheiro = models.IntegerField(null=False, blank=False)
    valor_banheiro = models.DecimalField(decimal_places=2, max_digits=5,
                                         null=False, blank=False)
    horas_cozinha = models.IntegerField(null=False, blank=False)
    valor_cozinha = models.DecimalField(decimal_places=2, max_digits=5,
                                        null=False, blank=False)
    horas_quintal = models.IntegerField(null=False, blank=False)
    valor_quintal = models.DecimalField(decimal_places=2, max_digits=5,
                                       null=False, blank=False)
    horas_outros = models.IntegerField(null=False, blank=False)
    valor_outros = models.DecimalField(decimal_places=2, max_digits=5,
                                       null=False, blank=False)
    icone = models.CharField(null=False, blank=False,
                             choices=ICONE_CHOICES, max_length=14)
    posicao = models.IntegerField(null=False)
# Create your models here.
