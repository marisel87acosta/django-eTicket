from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.


class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    dispo_legal = models.CharField(max_length=100)
    ley = models.IntegerField()
    articulo = models.IntegerField()
    inciso = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'categoria'

    def __unicode__(self):
        return (self.dispo_legal)

class Infraccion(models.Model):
    id_infr = models.AutoField(primary_key=True)
    id_cat = models.ForeignKey(Categoria, db_column='id_cat')
    id_mul = models.ForeignKey('Multa', db_column='id_mul')
    id_med = models.ForeignKey('Medicion', db_column='id_med')

    class Meta:
        managed = False
        db_table = 'infraccion'

    def __unicode__(self):
        return (self.id_cat)


class Infractor(models.Model):
    id_inf = models.AutoField(primary_key=True)
    dni = models.IntegerField()
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    sexo = models.CharField(max_length=1)
    domicilio = models.CharField(max_length=250)
    localidad = models.CharField(max_length=50)
    provincia = models.CharField(max_length=50)
    pais = models.CharField(max_length=30)
    cod_postal = models.IntegerField()
    licencia = models.CharField(max_length=15)
    clase = models.CharField(max_length=5)
    vence = models.DateField()

    class Meta:
        managed = False
        db_table = 'infractor'

    def __unicode__(self):
        return (self.dni)


class Medicion(models.Model):
    id_al = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    nro_serie = models.CharField(max_length=30)
    cod_aprobacion = models.IntegerField()
    valor = models.DecimalField(max_digits=3, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'medicion'

    def __unicode__(self):
        return (self.marca)


class Multa(models.Model):
    id_multa = models.AutoField(primary_key=True)
    fecha = models.DateField()
    hora = models.TimeField()
    id_infractor = models.ForeignKey(Infractor, db_column='id_infractor')
    id_usuario = models.ForeignKey('Usuario', db_column='id_usuario')
    id_vehiculo = models.ForeignKey('Vehiculo', db_column='id_vehiculo')
    partido = models.CharField(max_length=30)
    localidad = models.CharField(max_length=30)
    direccion = models.CharField(max_length=60)
    circulacion = models.CharField(max_length=12)
    retuvo_licencia = models.IntegerField()
    retuvo_vehiculo = models.IntegerField()
    observaciones = models.TextField()

    class Meta:
        managed = False
        db_table = 'multa'

    def __unicode__(self):
        return (self.fecha)


class Usuario(models.Model):
    id_usu = models.AutoField(primary_key=True)
    dni = models.IntegerField()
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=30)
    fech_nac = models.DateField()
    cel = models.IntegerField()
    us = models.CharField(max_length=20)
    pass_field = models.CharField(db_column='pass', max_length=15)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'usuario'

    def __unicode__(self):
        return (self.apellido)


class Vehiculo(models.Model):
    id_vehiculo = models.AutoField(primary_key=True)
    dominio = models.CharField(max_length=8)
    propietario = models.CharField(max_length=60)
    dni_propietario = models.IntegerField()
    marca = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    modelo = models.IntegerField()
    tipo = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'vehiculo'

    def __unicode__(self):
        return (self.dominio)
