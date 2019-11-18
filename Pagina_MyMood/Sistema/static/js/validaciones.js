

// Primero : asignar los eventos...
$(document).ready(function(){
	$("#form_registro").submit(function(evento){
		if(!validar()){
			alert("El formulario contiene errores");
			// Si el formulario no valida, no seguimos...
			evento.preventDefault();
		}
	})
});

function validar(){
	var valido = true;
	valido = valido && validarNombreCompleto(); 
	valido = valido && validarCorreo();
	valido = valido && validarSexo();
	valido = valido && validarDireccion();
	valido = valido && validarPais();
	return valido;
}

//Validar que los campos no esten vacios!!
function validarNombreCompleto() {
	var nombre = $("[name='nombre_completo']").val();
	nombre = $.trim(nombre); 
	if(nombre.length == 0)  {
		$("#mensaje_nombre_completo").html(
					"El nombre no debe quedar en blanco");		
	}
	return (nombre.length > 0);
}

function validarCorreo(){
	var correo = $("[name='correo']").val();
	correo = $.trim(correo);
	if (correo.length == 0) {
		$("#mensaje_correo").html("El correo no debe quedar en blanco");		
	}
	return (correo.length > 0);
}

function validarSexo() {
	var sexo = $("[name='sexo']").val();
	sexo = $.trim(sexo); 
	if(sexo.length == 0)  {
		$("#mensaje_sexo").html(
					"El sexo no debe quedar en blanco");		
	}
	return (sexo.length > 0);
}

function validarDireccion() {
	var direccion = $("[name='direccion']").val();
	direccion = $.trim(direccion); 
	if(direccion.length == 0)  {
		$("#mensaje_sexo").html(
					"El sexo no debe quedar en blanco");		
	}
	return (sexo.length > 0);
}

function validarPais() {
	var pais = $("[name='pais']").val();
	pais = $.trim(pais); 
	if(pais.length == 0)  {
		$("#mensaje_pais").html(
					"El pais no debe quedar en blanco");		
	}
	return (pais.length > 0);
}