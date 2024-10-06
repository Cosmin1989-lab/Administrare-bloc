from django.db import models

class Apartament(models.Model):
    numar = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.numar

class Locatar(models.Model):
    nume = models.CharField(max_length=100)
    apartament = models.ForeignKey(Apartament, on_delete=models.CASCADE, related_name='locatari')

    def __str__(self):
        return self.nume

class Factura(models.Model):
    locatar = models.ForeignKey(Locatar, on_delete=models.CASCADE, related_name='facturi')
    suma = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()


    def __str__(self):
        return f'Factura pentru {self.locatar.nume} - {self.suma} RON'
