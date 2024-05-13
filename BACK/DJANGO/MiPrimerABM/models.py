from django.db import models

# Create your models here.
class Administrador(models.Model):
    idusuario = models.AutoField(db_column='idUsuario', primary_key=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=45, blank=True, null=True)  # Field name made lowercase.
    fecha_registro = models.DateField(blank=True, null=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    direccion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'administrador'


