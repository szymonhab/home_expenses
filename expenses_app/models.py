from django.db import models


class Workspace(models.Model):

    def __str__(self):
        return self.id


class Category(models.Model):
    name = models.CharField(max_length=127)
    workspace = models.ForeignKey(Workspace)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=127)
    surname = models.CharField(max_length=127)
    workspace = models.ForeignKey(Workspace)

    def __str__(self):
        return self.name + ' ' + self.surname


class Shop(models.Model):
    name = models.CharField(max_length=127)

    def __str__(self):
        return self.name


class Bill(models.Model):
    bill_date = models.DateField()
    add_datetime = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    person = models.ForeignKey(Person)
    workspace = models.ForeignKey(Workspace)
    shop = models.ForeignKey(Shop, null=True)

    def __str__(self):
        return self.id


class BillRow(models.Model):
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    label = models.CharField(max_length=127)
    category = models.ForeignKey(Category)
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)

    def __str__(self):
        return self.id
