from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import CheckConstraint, Q, F

#-----------------------------------------------------------------------------------------------------------------#
#TABLA DE REGION
class Region(models.Model):
    id_region = models.AutoField(primary_key=True)
    nombre_region = models.CharField(max_length=45)

    def __str__(self):
        return self.nombre_region
    
#-----------------------------------------------------------------------------------------------------------------#
    
#TABLA DE PROVINCIA
class Provincia(models.Model):
    id_provincia = models.AutoField(primary_key=True)
    nombre_provincia = models.CharField(max_length=100)
    id_region =models.ForeignKey(Region, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre_provincia   

#-----------------------------------------------------------------------------------------------------------------# 
    
#TABLA DE COMUNA
class Comuna(models.Model):
    id_comuna = models.AutoField(primary_key=True)
    nombre_comuna = models.CharField(max_length=100)
    id_provincia = models.ForeignKey(Provincia, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre_comuna
    
#-----------------------------------------------------------------------------------------------------------------#

#TABLA LABORATORIO
class Laboratorio(models.Model):
    id_laboratorio = models.AutoField(primary_key=True)
    nombre_laboratorio = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_laboratorio

#-----------------------------------------------------------------------------------------------------------------#

#TABLA DE PRINCIPIO ACTIVO
class PrincipioActivo(models.Model):
    id_principio_activo= models.AutoField(primary_key=True)
    nombre_princio_activo = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_princio_activo        

#-----------------------------------------------------------------------------------------------------------------#

#TABLA DE ADMINISTRACION MEDICAMENTO
class ViaAdminstracion(models.Model):
    id_via_administracion = models.AutoField(primary_key=True)
    nombre_via_administracion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_via_administracion

#-----------------------------------------------------------------------------------------------------------------#

#TABLA DE FARMACIA
class Farmacia(models.Model):
    id_farmacia = models.AutoField(primary_key=True)
    marca_farmacia = models.CharField(max_length=200)

    def __str__(self):
        return self.marca_farmacia
    
#-----------------------------------------------------------------------------------------------------------------#

#TABLA DE MEDICAMENTOS
class Medicamentos(models.Model):
    id_medicamento = models.AutoField(primary_key=True)
    id_laboratorio = models.ForeignKey(Laboratorio, on_delete=models.PROTECT)
    id_principio_activo = models.ForeignKey(PrincipioActivo, on_delete=models.PROTECT)
    nombre_comercial = models.CharField(max_length=100)
    gramaje = models.CharField(max_length=50)
    cantidad_stock =models.IntegerField()
    presentacion_medicamento =models.CharField(max_length=100)
    id_via_administracion = models.ForeignKey(ViaAdminstracion, on_delete=models.PROTECT)
    #imagen = models.ImageField(upload_to="medicamentos", null=True)

    def __str__(self):
        return str(self.nombre_comercial)+" "+str(self.gramaje)
    
#-----------------------------------------------------------------------------------------------------------------#
    
#TABLA DE DESCUENTOS MEDICAMENTOS
class MedicamentosDescuento(models.Model):
    id_descuento = models.AutoField(primary_key=True)
    medicamento_desc = models.ForeignKey(Medicamentos, on_delete=models.PROTECT)
    id_farmacia = models.ForeignKey(Farmacia, on_delete=models.PROTECT)
    fecha_inicio_descuento = models.DateField()
    fecha_termino_descuento = models.DateField()
    descuento_porcentaje = models.IntegerField()

    def __str__(self):
        return str(self.medicamento_desc)+" con un %"+str(self.descuento_porcentaje)
    
#-----------------------------------------------------------------------------------------------------------------#

#TABLA DE MEDICAMENTO FICHA TECNICA
class MedicamentoFichaTecnica(models.Model):
    id_ficha_medicamento = models.AutoField(primary_key=True)
    laboratorio_ficha = models.ForeignKey(Laboratorio, on_delete=models.PROTECT)
    nombre_comercial = models.ForeignKey(Medicamentos, on_delete=models.PROTECT)
    url_ficha = models.CharField(max_length=700)

    def __str__(self):
        return self.url_ficha
    
#-----------------------------------------------------------------------------------------------------------------#

#TABLA TIPO DE USURIO
class Tipo_usuario(models.Model):
    id_TipoUsuario = models.AutoField(primary_key=True)
    nombre_tipo_usuario =models.CharField(max_length=100)
    def __str__(self):
        return self.nombre_tipo_usuario  

#-----------------------------------------------------------------------------------------------------------------#

#TABLA USUARIO
class Usuario(AbstractUser):

    rut_usuario = models.CharField(max_length=12)
    tipo_usuario = models.ForeignKey(Tipo_usuario, on_delete=models.PROTECT,null=True)

    def __str__(self):
        return str(self.first_name)+" "+str(self.last_name)+" "+str(self.rut_usuario)+" "+str(self.tipo_usuario)


#-----------------------------------------------------------------------------------------------------------------#

#TABLA USUARIO

class UsuarioFicha (models.Model):
    id_usuario = models.AutoField(primary_key=True)
    identificacion_usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL,null=True)
    dirreccion_usuario = models.CharField(max_length=150)
    email_usuario = models.EmailField()
    telefono_usuario = models.IntegerField()
    celular_usuario = models.IntegerField()
    whatsapp_usuario = models.IntegerField()
    telegram_usuario = models.IntegerField()
    id_comuna = models.ForeignKey(Comuna, on_delete=models.SET_NULL,null=True)
    #id_familiar = models.ForeignKey(Familiar, on_delete=models.PROTECT)
    def __str__(self):
        return str(self.identificacion_usuario)+" "+str(self.email_usuario)+" "+str(self.telefono_usuario)
       
#-----------------------------------------------------------------------------------------------------------------#

#-----------------------------------------------------------------------------------------------------------------#
#TABLA DE MEDICINA FRACCIONAMIENTO
#class MedicinaFraccionamiento(models.Model):
#    fraccion = models.CharField(max_length=10)
#    descripcion_fraccion = models.CharField(max_length=100)
#
#    def __str__(self):
#        return (self.fraccion)+" "+(self.descripcion_fraccion) 

#-----------------------------------------------------------------------------------------------------------------#

opciones_fraccionamiento = [
    [0,"1 Una pastilla entera"],
    [1,"1/4 Un quarto de pastilla"],
    [2,"1/2 Media Pastilla"],
    [3,"3/4 Tres cuartos de pastilla"],
    [4,"1/8 Un octavo de pastilla"]
]


#TABLA DE USUARIO RECETA
class PacienteReceta(models.Model):
    id_receta_usuario = models.AutoField(primary_key=True)
    fecha_receta = models.DateField()
    nombres_paciente = models.ForeignKey(Usuario, on_delete=models.SET_NULL,null=True)
    nombre_comercial = models.ForeignKey(Medicamentos, on_delete=models.SET_NULL,null=True)
    tiempo_tratamiento_dias = models.CharField(max_length=100)
    frecuencia_dosis_diaria = models.CharField(max_length=100)
    horario_1 = models.TimeField(null=True)
    fracionamiento_1 = models.IntegerField(choices=opciones_fraccionamiento, null=True)
    horario_2 = models.TimeField(blank=True ,null=True)
    fracionamiento_2 = models.IntegerField(choices=opciones_fraccionamiento,blank=True, null=True)
    horario_3 = models.TimeField(blank=True ,null=True)
    fracionamiento_3 = models.IntegerField(choices=opciones_fraccionamiento,blank=True, null=True)
    horario_4 = models.TimeField(blank=True ,null=True)
    fracionamiento_4 = models.IntegerField(choices=opciones_fraccionamiento,blank=True, null=True)
    horario_5 = models.TimeField(blank=True ,null=True)
    fracionamiento_5 = models.IntegerField(choices=opciones_fraccionamiento,blank=True, null=True)
    horario_6 = models.TimeField(blank=True ,null=True)
    fracionamiento_6 = models.IntegerField(choices=opciones_fraccionamiento,blank=True, null=True)
    descripcion = models.TextField()

    def __str__ (self):
        return str(self.nombres_paciente)+": "+str(self.nombre_comercial)+" Tratamiento por:"+str(self.tiempo_tratamiento_dias)+ "Dosis diaria"+str(self.frecuencia_dosis_diaria)

#-----------------------------------------------------------------------------------------------------------------#

#TABLA DE FAMILIAR
class PacienteFamiliar(models.Model):
    id_usuario_familiar = models.AutoField(primary_key=True)
    identificacion_familiar = models.ForeignKey(UsuarioFicha, on_delete=models.SET_NULL, null=True)
    parentesco = models.CharField(max_length=100)

    def __str__ (self):
        return  str(self.identificacion_familiar)+": "+str(self.parentesco)
#-----------------------------------------------------------------------------------------------------------------#

#TABLA DE USARIO FAMILAR PACIENTE
class FamiliarPacienteUsuario(models.Model):
    id_familiar_paciente = models.AutoField(primary_key=True)
    identificacion_familiar_paciente = models.ForeignKey(PacienteFamiliar, on_delete=models.SET_NULL, null=True)
    nombres_usuario = models.ForeignKey(UsuarioFicha, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.id_familiar_paciente)+" "+str(self.identificacion_familiar_paciente)


#-----------------------------------------------------------------------------------------------------------------#

#TABLA DE CESFAM
class CESFAM(models.Model):
    id_cesfam = models.AutoField(primary_key=True)
    identificacion_cesfam = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    email_CESFAM = models.CharField(max_length=200)
    telefono_CESFAM = models.CharField(max_length=200)
    direccion_CESFAM = models.CharField(max_length=200)
    nombre_comuna = models.ForeignKey(Comuna, on_delete=models.PROTECT)

    def __str__ (self):
        return str(self.identificacion_cesfam)+" "+str(self.direccion_CESFAM)+" "+str(self.nombre_comuna)+" tel:"+str(self.telefono_CESFAM)

#-----------------------------------------------------------------------------------------------------------------#

#TABLA DE QUIMICO FARMACEUTICO
class QuimicoFarmaceuticoEncargado(models.Model):
    id_quimico_farmaceutio = models.AutoField(primary_key=True)
    identificacion_QF = models.ForeignKey(Usuario, on_delete=models.SET_NULL,null=True)
    registro_sanitario_QF = models.CharField(max_length=200)

    def __str__(self):
        return str(self.identificacion_QF)+" "+str(self.registro_sanitario_QF)

#-----------------------------------------------------------------------------------------------------------------#

#TABLA DE SUCURSAL FARMACIA
class FarmaciaSucursal(models.Model):
    id_sucursal = models.AutoField(primary_key=True)
    nombre_farmacia = models.ForeignKey(Farmacia, on_delete=models.PROTECT)
    id_quimico_farmaceutio = models.ForeignKey(QuimicoFarmaceuticoEncargado ,on_delete= models.PROTECT)
    nombre_comuna = models.ForeignKey(Comuna, on_delete=models.PROTECT)
    direccion_sucursal = models.CharField(max_length=200)
    telefono_sucursal = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return str(self.nombre_farmacia)+" "+str(self.direccion_sucursal)+" "+str(self.nombre_comuna)+" tel:"+str(self.telefono_sucursal)

#-----------------------------------------------------------------------------------------------------------------#

#TABLA DE FARMACIA CESFAM
class FarmaciaCESFAM(models.Model):
    id_farmacia_CESFAM = models.AutoField(primary_key=True)
    identificacion_cesfam = models.ForeignKey(CESFAM, on_delete= models.PROTECT)
    

    def __str__(self):
        return str(self.identificacion_cesfam)

#-----------------------------------------------------------------------------------------------------------------#
opciones_diabetes = [
    [0,"No padezco esta enfermedad"],
    [1,"Prediabetes"],
    [2,"Diabetes tipo 1"],
    [3,"Diabetes tipo 2"],
    [4,"Diabetes gestacional"]
]
#-----------------------------------------------------------------------------------------------------------------#
opciones_hipertension = [
    [0,"No padezco esta enfermedad"],
    [1,"Hipertensión grado 1"],
    [2,"Hipertensión grado 2"],
    [3,"Hipertensión grado 3"]
]
#-----------------------------------------------------------------------------------------------------------------#

#TABLA DEL PACIENTE FICHA CLINICA
class PacienteFichaClinica(models.Model):
    id_paciente_ficha = models.AutoField(primary_key=True)
    identificacion_paciente = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    tipo_diabetes = models.IntegerField(choices=opciones_diabetes, null=True)
    tipo_hipertension = models.IntegerField(choices=opciones_hipertension, null=True)
    fecha_nacimiento = models.DateField()

    def __str__ (self):
        return str(self.identificacion_paciente)+ ": Diabetes:"+str(self.tipo_diabetes)+", Hipertension:"+str(self.tipo_hipertension)

#-----------------------------------------------------------------------------------------------------------------#

#OPCIONES DE CONSULTA EN CONTACTO
opciones_consulta = [
    [0,"Consulta"],
    [1,"Cotizacion"],
    [2,"Sugerencia"],
    [3,"Felicitaciones"],
    [4,"Reclamo"]
]

#TABLA DE CONTACTO
class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consulta, null=True)
    timestamp = models.CharField(max_length=100)
    mensaje = models.TextField()
    #registro_mensaje = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.nombre)

#-----------------------------------------------------------------------------------------------------------------#
#TABLA DE ENFERMERA
class Enfermera(models.Model):
    id_enfermera = models.AutoField(primary_key=True)
    identificacion_enfermera = models.ForeignKey(Usuario, on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return str(self.identificacion_enfermera)

#-----------------------------------------------------------------------------------------------------------------#
#TABLA PACIENTE PROFESIONALES
class ProfesionalPaciente(models.Model):
    identificacicion_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE,null=True ,related_name="Rpaciente",limit_choices_to=Q(tipo_usuario_id=3))
    identificacion_profesional = models.ForeignKey(Usuario, on_delete=models.CASCADE,null=True, related_name="Rprofesional",limit_choices_to=Q(tipo_usuario_id=2)| Q(tipo_usuario_id=7))
    ficha_clinica_paciente = models.ForeignKey(PacienteFichaClinica, on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return str(self.ficha_clinica_paciente)
