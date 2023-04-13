from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from import_export import resources
from import_export.admin import ImportExportModelAdmin




#-----------------------------------------------------------------------------------------------------------------#
#ADMIN DE REGION
class RegionAdmin(admin.ModelAdmin):
    list_display = ("id_region","nombre_region")
    search_fields = ["nombre_region"]

admin.site.register(Region, RegionAdmin)
#-----------------------------------------------------------------------------------------------------------------#
#ADMIN DE PROVINCIA
class ProvinciaAdmin(admin.ModelAdmin):
    list_display = ("id_provincia" ,"nombre_provincia")
    search_fields = ["nombre_provincia"]

admin.site.register(Provincia, ProvinciaAdmin)
#-----------------------------------------------------------------------------------------------------------------#
#ADMIN DE COMUNA
class ComunaAdmin(admin.ModelAdmin):
    list_display = ("id_comuna","nombre_comuna")
    search_fields = ["nombre_comuna"]

admin.site.register(Comuna, ComunaAdmin)
#-----------------------------------------------------------------------------------------------------------------#
#ADMIN DE LABORATORIO
class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ("id_laboratorio","nombre_laboratorio")
    search_fields = ["nombre_laboratorio"]

admin.site.register(Laboratorio, LaboratorioAdmin)
#-----------------------------------------------------------------------------------------------------------------#
#ADMIN DE PRINCIPIO ACTIVO
class PrincipioActivoAdmin(admin.ModelAdmin):
    list_display = ("id_principio_activo","nombre_princio_activo")
    search_fields = ["nombre_princio_activo"]

admin.site.register(PrincipioActivo, PrincipioActivoAdmin)
#-----------------------------------------------------------------------------------------------------------------#
#ADMIN DE VIA ADMINISTRACION
class ViaAdministracionAdmin(admin.ModelAdmin):
    list_display = ("id_via_administracion","nombre_via_administracion")
    search_fields = ["nombre_via_administracion"]

admin.site.register(ViaAdminstracion, ViaAdministracionAdmin)
#-----------------------------------------------------------------------------------------------------------------#
#ADMIN DE TIPO FARMACIA
class FarmaciaAdmin(admin.ModelAdmin):
    list_display = ("id_farmacia", "marca_farmacia")
    search_fields = ["marca_farmacia"]

admin.site.register(Farmacia, FarmaciaAdmin)
#-----------------------------------------------------------------------------------------------------------------#
#ADMIN DE TIPO MEDICAMENTOS
class MedicamentosAdmin(admin.ModelAdmin):
    list_display = ("id_medicamento", "id_laboratorio", "id_principio_activo", "nombre_comercial",  "gramaje", "cantidad_stock", "presentacion_medicamento", "id_via_administracion")
    search_fields = ["nombre_comercial", "id_medicamento", "id_laboratorio"]

admin.site.register(Medicamentos, MedicamentosAdmin)
#-----------------------------------------------------------------------------------------------------------------#
class MedicamentosDescuentoAdmin(admin.ModelAdmin):
    list_display = ("id_descuento", "medicamento_desc", "id_farmacia", "fecha_inicio_descuento",  "fecha_termino_descuento", "descuento_porcentaje")
    search_fields = ["id_descuento", "medicamento_desc", "id_farmacia", "fecha_inicio_descuento",  "fecha_termino_descuento", "descuento_porcentaje"]

admin.site.register(MedicamentosDescuento, MedicamentosDescuentoAdmin)
#-----------------------------------------------------------------------------------------------------------------#
#ADMIN DE MEDICAMENTO FICHA TECNICA
class MedicamentoFichaTecnicaAdmin(admin.ModelAdmin):
    list_display = ("id_ficha_medicamento", "nombre_comercial", "url_ficha")
    search_fields = ["id_ficha_medicamento", "nombre_comercial", "url_ficha"]

admin.site.register(MedicamentoFichaTecnica, MedicamentoFichaTecnicaAdmin)
#-----------------------------------------------------------------------------------------------------------------#
#ADMIN DE TIPO USUARIO
class Tipo_usuarioAdmin(admin.ModelAdmin):
    list_display = ("id_TipoUsuario", "nombre_tipo_usuario")
    search_fields = ["nombre_tipo_usuario"]

admin.site.register(Tipo_usuario, Tipo_usuarioAdmin)
#-----------------------------------------------------------------------------------------------------------------#
#ADMIN DE USUARIO
class UserAdmin(BaseUserAdmin): 
    list_display = ('id','tipo_usuario','username','password', 'email', 'rut_usuario', 'first_name','last_name') 
    list_filter = ('email',)
    list_editable = ('password',) 
    fieldsets = ( 
        (None,{'fields': ('username','email', 'password')}), 
        ('Informacion personal', {'fields': ( 'first_name', 'last_name', 'tipo_usuario','rut_usuario')}), 
        ('Permisos Django', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups')})  
    ) 
 
    add_fieldsets = (
        (None, {
            'classes':('wide',),
            'fields':('tipo_usuario','rut_usuario'  ,'username', 'email', 'first_name', 'last_name', 'password1', 'password2')
        }
    ),  # <-- add this comma!
    )
admin.site.register(Usuario, UserAdmin)
#-----------------------------------------------------------------------------------------------------------------#
#ADMIN DE USUARIO FICHA ADMIN
class UsuarioFichaAdmin(admin.ModelAdmin):
    list_display = ('id_usuario', 'identificacion_usuario', 'dirreccion_usuario', 'email_usuario', 'telefono_usuario', 'celular_usuario', 'whatsapp_usuario','telegram_usuario','id_comuna')
    search_fields = ['id_usuario', 'identificacion_usuario', 'dirreccion_usuario', 'email_usuario', 'telefono_usuario', 'celular_usuario', 'whatsapp_usuario','telegram_usuario','id_comuna']

admin.site.register(UsuarioFicha, UsuarioFichaAdmin)
#-----------------------------------------------------------------------------------------------------------------#
#ADMIN DE MEDICINA FRACCIONAMIENTO
#class MedicinaFraccionamientoResouce(resources.ModelResource):
#    class Meta:
#        model = MedicinaFraccionamiento
#
#class MedicinaFraccionamientoAdmin(ImportExportModelAdmin):
#    resource_class = MedicinaFraccionamientoResouce

#admin.site.register(MedicinaFraccionamiento, MedicinaFraccionamientoAdmin)
#-----------------------------------------------------------------------------------------------------------------#
#ADMIN DE USUARIO RECETA
class PacienteRecetaAdmin(admin.ModelAdmin):
    list_display = ('id_receta_usuario', 'fecha_receta', 'nombres_paciente', 'nombre_comercial','tiempo_tratamiento_dias', 'frecuencia_dosis_diaria','fracionamiento_1' , 'horario_1','fracionamiento_2','horario_2','horario_3','fracionamiento_3','horario_4','fracionamiento_4','horario_5','fracionamiento_5','horario_6','fracionamiento_6', 'descripcion')
    search_fields = ['id_receta_usuario', 'fecha_receta', 'nombres_paciente', 'nombre_comercial','tiempo_tratamiento_dias', 'frecuencia_dosis_diaria','fracionamiento_1' , 'horario_1','fracionamiento_2','horario_2','horario_3','fracionamiento_3','horario_4','fracionamiento_4','horario_5','fracionamiento_5','horario_6','fracionamiento_6', 'descripcion']

admin.site.register(PacienteReceta, PacienteRecetaAdmin)
#-----------------------------------------------------------------------------------------------------------------#
#TABLA DE USUARIO FAMILIAR
class PacienteFamiliarAdmin(admin.ModelAdmin):
    list_display  = ('id_usuario_familiar','identificacion_familiar','parentesco')
    search_fields = ['id_usuario_familiar','identificacion_familiar','parentesco']

admin.site.register(PacienteFamiliar, PacienteFamiliarAdmin)
#-----------------------------------------------------------------------------------------------------------------#
#ADMIN DE USUARIO FARMACO VIGILANGIA
class FamiliarPacienteUsuarioAdmin(admin.ModelAdmin):
    list_display  = ('id_familiar_paciente', 'identificacion_familiar_paciente', 'nombres_usuario')
    search_fields = ['id_familiar_paciente', 'identificacion_familiar_paciente', 'nombres_usuario']

admin.site.register(FamiliarPacienteUsuario, FamiliarPacienteUsuarioAdmin)
#-----------------------------------------------------------------------------------------------------------------#
#ADMIN DE CESFAM
class CESFAMAdmin(admin.ModelAdmin):
    list_display = ('id_cesfam', 'identificacion_cesfam', 'email_CESFAM', 'telefono_CESFAM', 'direccion_CESFAM', 'nombre_comuna')
    search_fields = ['id_cesfam', 'identificacion_cesfam', 'email_CESFAM', 'telefono_CESFAM', 'direccion_CESFAM', 'nombre_comuna']

admin.site.register(CESFAM, CESFAMAdmin)
#-----------------------------------------------------------------------------------------------------------------#
#ADMIN DE ENCARGADO QUIMICO FARMACEUTICO
class QuimicoFarmaceuticoEncargadoAdmin(admin.ModelAdmin):
    list_display = ('id_quimico_farmaceutio', 'identificacion_QF', 'registro_sanitario_QF')
    search_fields = ['id_quimico_farmaceutio', 'identificacion_QF', 'registro_sanitario_QF']

admin.site.register(QuimicoFarmaceuticoEncargado, QuimicoFarmaceuticoEncargadoAdmin)
#-----------------------------------------------------------------------------------------------------------------#
#ADMIN DE TIPO FARMACIA SUCURSAL
class FarmaciaSucursalAdmin(admin.ModelAdmin):
    list_display = ("id_sucursal", "nombre_farmacia", "id_quimico_farmaceutio", "nombre_comuna", "direccion_sucursal", "telefono_sucursal", "email")
    search_fields = ["id_sucursal", "nombre_farmacia", "id_quimico_farmaceutio", "nombre_comuna", "direccion_sucursal", "telefono_sucursal", "email"]

admin.site.register(FarmaciaSucursal, FarmaciaSucursalAdmin)
#-----------------------------------------------------------------------------------------------------------------#
#ADMIN DE TIPO FARMACIA CESFAM
class FarmaciaCESFAMAdmin(admin.ModelAdmin):
    list_display = ('id_farmacia_CESFAM', 'identificacion_cesfam')
    search_fields = ['id_farmacia_CESFAM', 'identificacion_cesfam']

admin.site.register(FarmaciaCESFAM, FarmaciaCESFAMAdmin)
#-----------------------------------------------------------------------------------------------------------------#
#ADMIN DE USUARIO FARMACO VIGILANGIA
class PacienteFichaClinicaAdmin(admin.ModelAdmin):
    list_display  = ('id_paciente_ficha', 'identificacion_paciente','tipo_diabetes','tipo_hipertension', 'fecha_nacimiento')
    search_fields = ['id_paciente_ficha', 'identificacion_paciente','tipo_diabetes','tipo_hipertension', 'fecha_nacimiento']

admin.site.register(PacienteFichaClinica, PacienteFichaClinicaAdmin)
#-----------------------------------------------------------------------------------------------------------------#
#ADMIN DE CONTACTO
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'tipo_consulta', 'timestamp', 'mensaje')
    search_fields = ['nombre', 'email', 'tipo_consulta', 'timestamp', 'mensaje']
admin.site.register(Contacto, ContactoAdmin)
#-----------------------------------------------------------------------------------------------------------------#
#ADMIN DE ENFERMERA
class EnfermeraAdmin(admin.ModelAdmin):
    list_display = ('id_enfermera','identificacion_enfermera')
    search_fields = ['id_enfermera','identificacion_enfermera']
admin.site.register(Enfermera, EnfermeraAdmin)
#-----------------------------------------------------------------------------------------------------------------#
#ADMIN DE PACIENTE PROFESIONAL
class ProfesionalPacienteAdmin(admin.ModelAdmin):
    list_display = ('identificacicion_usuario','identificacion_profesional' , 'ficha_clinica_paciente')
    search_fields = ['identificacicion_usuario','identificacion_profesional' , 'ficha_clinica_paciente']
admin.site.register(ProfesionalPaciente, ProfesionalPacienteAdmin)