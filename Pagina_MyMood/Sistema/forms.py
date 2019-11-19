from django import forms
SEXOS=(('Femenino','Masculino'))
#Formulario para Registro de la Persona

class RegistrarPersonaForm(forms.Form):
    rutPersona=forms.CharField(widget=forms.TextInput(),label="Rut")
    passwordPersona=forms.CharField(widget=forms.PasswordInput(),label="Contraseña")
    nombreCompleto=forms.CharField(widget=forms.TextInput(),label="Nombre Completo")
    mailPersona=forms.EmailField(label="Email: ")
    fechaNacimiento=forms.DateField(widget=forms.SelectDateWidget(years=range(1910,2001)),label="Fecha de Nacimiento")
    pais=forms.CharField(widget=forms.TextInput(),label="Pais")
    sexo=forms.ChoiceField(choices=(SEXOS),label="Sexo")

# Formulario para Registro de una Persona DESDE EL ADMIN
class RegistrarAdminForm(forms.Form):
    rutPersona=forms.CharField(widget=forms.TextInput(),label="Rut")
    passwordPersona=forms.CharField(widget=forms.PasswordInput(),label="Contraseña")
    nombrePersona=forms.CharField(widget=forms.TextInput(),label="Nombre")
    apellidoPersona=forms.CharField(widget=forms.TextInput(),label="Apellido")
    mailPersona=forms.EmailField(label="Email: ")
    fechaNacimiento=forms.DateField(widget=forms.SelectDateWidget(years=range(1910,2001)),label="Fecha de Nacimiento")
    numeroFono=forms.CharField(widget=forms.TextInput(),label="Telefono")    
    sexo=forms.ChoiceField(choices=(SEXOS),label="Sexos")

# Formulario para el Login
class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(),label="Rut de Usuario")
    password=forms.CharField(widget=forms.PasswordInput(),label="Contraseña")    

# Formulario para Email Restablece Contraseña
class RecuperacionForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(),label="Rut")

# Formulario para Restablecer Contraseña
class RestablecerForm(forms.Form):
    password_A=forms.CharField(widget=forms.PasswordInput(),label="Nueva Contraseña")
    password_B=forms.CharField(widget=forms.PasswordInput(),label="Repita Contraseña")
    