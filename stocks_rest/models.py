from django.db import models

class SP500(models.Model):
    symbol = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50, unique=True)
    momentum_12_2 = models.FloatField()
    p_e = models.FloatField(null=True)
    e_p = models.FloatField(null=True)

    def __str__(self):
        return f'{[self.symbol, self.name]}'

class DJ30(models.Model):
    symbol = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50, unique=True)
    momentum_12_2 = models.FloatField()
    p_e = models.FloatField(null=True)
    e_p = models.FloatField(null=True)
    p_div = models.FloatField(null=True)

    def __str__(self):
        return f'{[self.symbol, self.name]}'

class Div(models.Model):
    symbol = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50, unique=True)
    p_div = models.FloatField(null=True)

    def __str__(self):
        return f'{[self.symbol, self.name]}'

class Index(models.Model):
    symbol = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50, unique=True)
    momentum = models.FloatField(null=True)
    ma10 = models.FloatField(null=True)
    avg_pe = models.FloatField(null=True)

    def __str__(self):
        return f'{[self.symbol, self.name]}'
