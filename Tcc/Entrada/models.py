from django.db import models

# Create your models here.
class Mensage(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=20, decimal_places=0)
    mensage = models.CharField(max_length=400, blank=True)
    id_user = models.CharField(max_length=150, blank=True)
    key = models.ForeignKey("self", related_name="self", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.id}'
