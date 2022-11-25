from django.db import models


class Item(models.Model):
    name = models.CharField('Nome', max_length=100)
    value = models.DecimalField('Valor', decimal_places=2, max_digits=9)
    created_at = models.DateField('Criado em', auto_now=True)
    updated_at = models.DateField('Modificado em',auto_now_add=True)
    active = models.BooleanField('Ativo', default=True)
    obs = models.TextField('Observação', blank=True, null=True)

    def __str__(self):
        return self.name    
    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'

    def get_created_at(self):
        return self.created_at.strftime("%d/%m/%Y")

    def get_updated_at(self):
        return self.updated_at.strftime("%d/%m/%Y")


class Waiter(models.Model):
    name = models.CharField(max_length=100)
    commission = models.DecimalField(decimal_places=2, max_digits=9)
    created_at = models.DateField('Criado em', auto_now=True)
    updated_at = models.DateField('Modificado em',auto_now_add=True)
    active = models.BooleanField('Ativo', default=True)

    def __str__(self):
        return self.name

    def get_created_at(self):
        return self.created_at.strftime("%d/%m/%Y")

    def get_updated_at(self):
        return self.updated_at.strftime("%d/%m/%Y")


class Comand(models.Model):
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    percents = models.DecimalField(decimal_places=2, max_digits=9)
    created_at = models.DateField('Criado em', auto_now=True)
    updated_at = models.DateField('Modificado em',auto_now_add=True)

    def __str__(self):
        return self.item_id

    def get_created_at(self):
        return self.created_at.strftime("%d/%m/%Y")

    def get_updated_at(self):
        return self.updated_at.strftime("%d/%m/%Y")

