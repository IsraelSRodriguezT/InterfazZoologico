from django.db import models
from datetime import datetime,date
from enum import Enum

from django.db.models import PositiveIntegerField


# Create your models here.
# Enumeradores:
class Estado(Enum):
    NORMAL = "NORMAL"
    DESCANSANDO = "DESCANSANDO"
    ENFERMO = "ENFERMO"
    HERIDO = "HERIDO"
    ESTRESADO = "ESTRESADO"
    HAMBRIENTO = "HAMBRIENTO"
    COMIENDO = " COMIENDO"

class TipoAlimento(Enum):
    CARNE = "CARNE"
    PESCADO = "PESCADO"
    HIERBA = "HIERBA"
    FRUTA = "FRUTA"

class TipoCuerpo(Enum):
    INVERTEBRADO = "INVERTEBRADO"
    VERTEBRADO = "VERTEBRADO"

class TipoDieta(Enum):
    CARNIVORO = "CARNIVORO"
    HERVIVORO = "HERVIVORO"
    OMNIVORO = "OMNIVORO"

class Zona(Enum):
    NORTE = "NORTE"
    SUR = "SUR"
    ESTE = "ESTE"
    OESTE = "OESTE"

# Clases
class SerVivo(models.Model):
    # Atributos:
    fecha_nacimiento = models.DateField()
    nombre = models.CharField(max_length=100)
    class Meta:
        abstract = True
    # Metodos:
    def calcular_edad(self):
        fecha_actual = date.today()
        if self.fecha_nacimiento and self.fecha_nacimiento <= fecha_actual:
            edad = fecha_actual.year - self.fecha_nacimiento.year - (
                    (fecha_actual.month, fecha_actual.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day)
            )
            return edad
        return None

class Animal(SerVivo):
    # Atributos:
    nombre_cientifico = models.CharField(max_length=100)
    edad = PositiveIntegerField(null=True,editable=False)
    peso = models.FloatField()
    # Asociacion:
    zoologico = models.ForeignKey('Zoologico', on_delete=models.CASCADE, related_name='animales', null=True)
    jaula = models.ForeignKey('Jaula', on_delete=models.CASCADE, related_name='animales', null=True)
    cuidador = models.ForeignKey('Cuidador', on_delete=models.CASCADE, related_name='animales', null=True)
    veterinario = models.ForeignKey('Veterinario', on_delete=models.CASCADE, related_name='animales', null=True)
    # Enumeradores:
    estado = models.CharField(max_length=50, choices=[(tag.value, tag.name) for tag in Estado], null = True)
    tipo_cuerpo = models.CharField(max_length=50, choices=[(tag.value, tag.name) for tag in TipoCuerpo], null = True)
    tipo_dieta = models.CharField(max_length=50, choices=[(tag.value, tag.name) for tag in TipoDieta], null = True)
    zona = models.CharField(max_length=50, choices=[(tag.value, tag.name) for tag in Zona], null = True)
    class Meta:
        verbose_name = 'Animal'
        verbose_name_plural = 'Animales'
    # Metodos:
    def save(self, *args, **kwargs):
        self.edad = self.calcular_edad()
        super().save(*args, **kwargs)
    def __str__(self):
        return self.nombre+' | '+self.nombre_cientifico

class Persona(SerVivo):
    # Atributos:
    edad = PositiveIntegerField(null=True, editable=False)
    cedula = models.CharField(max_length=10, unique=True, verbose_name='Cedula:')
    class Meta:
        abstract = True
    # Metodos:
    def save(self, *args, **kwargs):
        self.edad = self.calcular_edad()
        super().save(*args, **kwargs)

class Empleado(Persona):
    # Atributos:
    identificacion = models.CharField(max_length=7, unique=True, editable=False)
    salario = models.FloatField()
    zona = models.CharField(max_length=50, choices=[(tag.value, tag.name) for tag in Zona], null = True)
    class Meta:
        abstract = True

class Cuidador(Empleado):
    # Asociacion:
    zoologico = models.ForeignKey('Zoologico', on_delete=models.CASCADE, related_name='cuidadores', null=True)
    class Meta:
        verbose_name = 'Cuidador'
        verbose_name_plural = 'Cuidadores'
    # Metodos:
    def save(self, *args, **kwargs):
        if not self.identificacion:
            if not self.zona:
                raise ValueError("! Se debe asignar una zona antes de asignar el empleado !")
            letra_zona = self.zona[0].upper()
            empleados_zona = Cuidador.objects.filter(zona=self.zona).count() + 1
            self.identificacion = f"11C{letra_zona}{empleados_zona:02d}"
        super().save(*args, **kwargs)
    def __str__(self):
        return self.nombre+' | '+ self.identificacion

class Veterinario(Empleado):
    # Atributos:
    especialidad = models.CharField(max_length=100)
    # Asociacion:
    zoologico = models.ForeignKey('Zoologico', on_delete=models.CASCADE, related_name='veterinarios', null=True)
    # Metodos:
    def save(self, *args, **kwargs):
        if not self.identificacion:
            if not self.zona:
                raise ValueError("! Se debe asignar una zona antes de asignar el empleado !")
            letra_zona = self.zona[0].upper()
            empleados_zona = Veterinario.objects.filter(zona=self.zona).count() + 1
            self.identificacion = f"11V{letra_zona}{empleados_zona:02d}"
        super().save(*args, **kwargs)
    def __str__(self):
        return self.nombre + ' | ' + self.identificacion

class PersonalLimpieza(Empleado):
    # Asociacion:
    zoologico = models.ForeignKey('Zoologico', on_delete=models.CASCADE, related_name='personal_limpieza_list', null=True)
    class Meta:
        verbose_name = 'Personal de Limpieza'
        verbose_name_plural = 'Personales de Limpieza'
    # Metodos:
    def limpiar_jaulas(self):
        pass
    def save(self, *args, **kwargs):
        if not self.identificacion:
            if not self.zona:
                raise ValueError("! Se debe asignar una zona antes de asignar el empleado !")
            letra_zona = self.zona[0].upper()
            empleados_zona = PersonalLimpieza.objects.filter(zona=self.zona).count() + 1
            self.identificacion = f"11L{letra_zona}{empleados_zona:02d}"
        super().save(*args, **kwargs)
    def __str__(self):
        return self.nombre + ' | ' + self.identificacion

class Guia(Empleado):
    # Atributos:
    zoologico = models.ForeignKey('Zoologico', on_delete=models.CASCADE, related_name='guias', null=True)
    # Metodos:
    def establecer_recorrido(self):
        pass
    def save(self, *args, **kwargs):
        if not self.identificacion:
            if not self.zona:
                raise ValueError("! Se debe asignar una zona antes de asignar el empleado !")
            letra_zona = self.zona[0].upper()
            empleados_zona = Guia.objects.filter(zona=self.zona).count() + 1
            self.identificacion = f"11G{letra_zona}{empleados_zona:02d}"
        super().save(*args, **kwargs)
    def __str__(self):
        return self.nombre+' | '+ self.identificacion

class Jaula(models.Model):
    # Atributos:
    capacidad = models.PositiveIntegerField()
    numero = models.CharField(max_length=7, unique=True, editable=False)
    esta_limpio = models.BooleanField(null = True, verbose_name='Esta limpio')
    zona = models.CharField(max_length=50, choices=[(tag.value, tag.name) for tag in Zona], null=True)
    # Asociacion:
    personal_limpieza = models.ForeignKey(PersonalLimpieza, on_delete=models.CASCADE, related_name='jaulas',
                                          null=True, verbose_name='Personal limpieza:')
    class Meta:
        verbose_name = 'Jaula'
        verbose_name_plural = 'Jaulas'
    # Metodos:
    def save(self, *args, **kwargs):
        if not self.numero:
            if not self.zona:
                raise ValueError("! Se debe asignar una zona antes de guardar la jaula !")
            letra_zona = self.zona[0].upper()
            jaulas_zona = Jaula.objects.filter(zona=self.zona).count() + 1
            self.numero = f"14{letra_zona}{jaulas_zona:02d}"
        super().save(*args, **kwargs)
    def __str__(self):
        return 'Jaula: '+self.numero+' | Capacidad: '+str(self.capacidad)

class Cliente(Persona):
    # Asociacion:
    zoologico = models.ForeignKey('Zoologico', on_delete=models.CASCADE, related_name='clientes', null=True)
    guia = models.ForeignKey(Guia, on_delete=models.CASCADE, related_name='clientes', null=True)
    # Metodos:
    def __str__(self):
        return self.nombre+' | '+ self.cedula

class Boleto(models.Model):
    # Atributos:
    fecha_visita = models.DateField(auto_now=True, verbose_name='Fecha de visita')
    numero = models.CharField(max_length=7, unique=True, editable=False)
    valor = 2.5
    # Asociacion:
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE, related_name='boleto', null=True)
    compra = models.ForeignKey('Compra', on_delete=models.CASCADE, related_name='boletos', null=True)
    class Meta:
        verbose_name = 'Boleto'
        verbose_name_plural = 'Boletos'
    # Metodos:
    def calcular_valor(self):
        if not self.cliente:
            raise ValueError("¡El boleto no está asociado a un cliente!")
        edad_cliente = self.cliente.calcular_edad()
        if edad_cliente < 18 or edad_cliente >= 65:
            return self.valor / 2  
        return self.valor 
    def save(self, *args, **kwargs):
        if not self.cliente:
            raise ValueError("! El boleto no esta asociado a un cliente !")
        if not self.numero:
            boletos_existentes = Boleto.objects.count() + 1
            self.numero = f"{boletos_existentes:06d}"
        super().save(*args, **kwargs)
    def __str__(self):
        return ('Boleto: '+self.numero+' | Valor: '+str(self.calcular_valor())+'$ | Cliente:'+self.cliente.nombre+
                ' | Fecha: '+str(self.fecha_visita))

class Compra(models.Model):
    class Meta:
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'
    # Metodos:
    def calcular_total(self):
        total = 0
        boletos = Boleto.objects.filter(compras=self)
        for boleto in boletos:
            total += boleto.calcular_valor()
        return total
    def __str__(self):
        return f"Compra: {self.id} | Total: {self.calcular_total()}$"

class Direccion(models.Model):
    # Atributos:
    calle_principal = models.CharField(max_length=100, verbose_name="Calle principal")
    calle_secundaria = models.CharField(max_length=100, verbose_name="Calle secundaria")
    referencia = models.CharField(max_length=100, verbose_name="Referencia")
    class Meta:
        verbose_name = 'Direccion'
        verbose_name_plural = 'Direcciones'
    # Metodos:
    def __str__(self):
        return f"Direccion: {self.calle_principal} y {self.calle_secundaria} | {self.referencia}"

class Zoologico(models.Model):
    # Atributos:
    capacidad = models.PositiveIntegerField()
    nombre = models.CharField(max_length=100, unique=True)
    telefono = models.CharField(max_length=10, unique=True)
    # Asociacion:
    direccion = models.OneToOneField(Direccion, on_delete=models.CASCADE, null=True)
    class Meta:
        verbose_name = "Zoológico"
        verbose_name_plural = "Zoológicos"
    # Metodos:
    def __str__(self):
        return self.nombre+' | Capacidad: '+str(self.capacidad)

class HistorialMedico(models.Model):
    # Atributos:
    diagnostico = models.TextField()
    fecha = models.DateField(auto_now=True)
    # Asociacion:
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='historial_medico_list', null=True)