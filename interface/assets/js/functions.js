// exposed functions
eel.expose(recebe_resistencia);

// Print at python console
eel.pythonPrint("connected!"); 

// Setup functions

// Config functions

// Comunication functions

// Calib functions

// Index functions
function verifica_escala(){
	return document.getElementById('escala-select').value
}


function solicita_resitencia(){
    eel.solicita_resitencia(verifica_escala());
}


function adjust_multiplier(value){
	let len = value.length

	if (value[len-1] == 'Ω'){
		value = value.substring(0, len-1);
		len = value.length
	}

	if (value[len-1] == 'u'){
		value = (value.substring(0, len-1))/1000000;
		return (value)
	}
	if (value[len-1] == 'm'){
		value = (value.substring(0, len-1))/1000;
		return (value)
	}
	else{
		return value
	}

}


function verifica_limites(){
	resistance_min = adjust_multiplier(document.getElementById('Rmin').value)
	resistance_max = adjust_multiplier(document.getElementById('Rmax').value)
	resistance_read = adjust_multiplier(document.getElementById('resistance-field').value)

	eel.pythonPrint(resistance_min)
	eel.pythonPrint(resistance_max)
	eel.pythonPrint(resistance_read)

	
	if (resistance_min > resistance_read){
		document.getElementById('Rmax').style.background = "white"
		document.getElementById('Rmin').style.background = "red"
	}
	else if (resistance_read > resistance_max){
		document.getElementById('Rmax').style.background = "red"
		document.getElementById('Rmin').style.background = "white"
	}
	else {
		document.getElementById('Rmax').style.background = "green"
		document.getElementById('Rmin').style.background = "green"
	}
}


function recebe_resistencia(value){
    document.getElementById('resistance-field').value = value
    verifica_limites()
}