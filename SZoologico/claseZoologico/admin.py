from django.contrib import admin
from .models import Animal,Jaula,Boleto,Compra,Cliente,Cuidador,Veterinario,PersonalLimpieza,Guia,Direccion,Zoologico
# Register your models here.
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('nombre','nombre_cientifico','edad','peso','jaula','cuidador','veterinario','estado','tipo_cuerpo',
                    'tipo_dieta','zona')
    list_filter = ('jaula','cuidador','veterinario','estado','tipo_cuerpo','tipo_dieta','zona')
    search_fields = ('nombre','nombre_cientifico')
admin.site.register(Animal,AnimalAdmin)
class JaulaAdmin(admin.ModelAdmin):
    list_display = ('capacidad','numero','esta_limpio','zona','personal_limpieza')
    list_filter = ('capacidad','esta_limpio','zona','personal_limpieza')
    search_fields = ('numero',)
admin.site.register(Jaula,JaulaAdmin)
class BoletoAdmin(admin.ModelAdmin):
    list_display = ('numero','fecha_visita','cliente','compra')
    list_filter = ('fecha_visita','cliente','compra')
    search_fields = ('numero',)
admin.site.register(Boleto,BoletoAdmin)
class CompraAdmin(admin.ModelAdmin):
    list_display = ('id',)
    search_fields = ('id',)
admin.site.register(Compra,CompraAdmin)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre','edad','cedula','guia')
    list_filter = ('guia','edad')
    search_fields = ('nombre','cedula')
admin.site.register(Cliente,ClienteAdmin)
class CuidadorAdmin(admin.ModelAdmin):
    list_display = ('nombre','edad','cedula','identificacion','salario','zona')
    list_filter = ('zona',)
    search_fields = ('nombre','cedula','identificacion')
admin.site.register(Cuidador,CuidadorAdmin)
class VeterinarioAdmin(admin.ModelAdmin):
    list_display = ('nombre','edad','cedula','identificacion','salario','zona','especialidad')
    list_filter = ('zona',)
    search_fields = ('nombre','cedula','identificacion')
admin.site.register(Veterinario,VeterinarioAdmin)
class PersonalLimpiezaAdmin(admin.ModelAdmin):
    list_display = ('nombre','edad','cedula','identificacion','salario','zona')
    list_filter = ('zona',)
    search_fields = ('nombre','cedula','identificacion')
admin.site.register(PersonalLimpieza,PersonalLimpiezaAdmin)
class GuiaAdmin(admin.ModelAdmin):
    list_display = ('nombre','edad','cedula','identificacion','salario','zona')
    list_filter = ('zona',)
    search_fields = ('nombre','cedula','identificacion')
admin.site.register(Guia,GuiaAdmin)
class DireccionAdmin(admin.ModelAdmin):
    list_display = ('calle_principal','calle_secundaria','referencia')
    search_fields = ('calle_principal','calle_secundaria')
admin.site.register(Direccion,DireccionAdmin)
class ZoologicoAdmin(admin.ModelAdmin):
    list_display = ('nombre','capacidad','telefono','direccion')
    list_filter = ('capacidad',)
    search_fields = ('nombre','telefono')
admin.site.register(Zoologico,ZoologicoAdmin)