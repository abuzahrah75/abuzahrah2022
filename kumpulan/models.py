from django.db import models

class Kumpulan(models.Model):
    nama = models.CharField(max_length=250)
    st_flag = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.nama}'


class Jenis(models.Model):
    nama = models.CharField(max_length=250)
    st_flag = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.nama}'


class Kategori(models.Model):
    nama = models.CharField(max_length=250)
    st_flag = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.nama}'


class Tags(models.Model):
    nama = models.CharField(max_length=250)
    st_flag = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.nama}'
