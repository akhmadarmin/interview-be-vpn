from django.db import models
from django.contrib.auth.models import User

class DataPengguna(models.Model):
    nama = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=40)
    no_hp = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Data Pengguna'

    def __str__(self):
        return f"{self.nama} - {self.email}"