// exposed functions
eel.expose(recebe_resistencia);
eel.expose(update_calib_data);

// Print at python console
eel.pythonPrint("connected!"); 

// Setup functions

// Config functions

// Comunication functions

// Calib functions
function calib_page_loaded(){
	eel.read_calib()    
}

function update_calib_data(calib_data){
	document.getElementById('offset-1').value = calib_data[1]['offset']
    document.getElementById('gain-1').value = calib_data[1]['gain']
    document.getElementById('offset-2').value = calib_data[2]['offset']
    document.getElementById('gain-2').value = calib_data[2]['gain']
    document.getElementById('offset-3').value = calib_data[3]['offset']
    document.getElementById('gain-3').value = calib_data[3]['gain']
    document.getElementById('offset-4').value = calib_data[4]['offset']
    document.getElementById('gain-4').value = calib_data[4]['gain']
    document.getElementById('offset-5').value = calib_data[5]['offset']
    document.getElementById('gain-5').value = calib_data[5]['gain']
    document.getElementById('offset-6').value = calib_data[6]['offset']
    document.getElementById('gain-6').value = calib_data[6]['gain']
    document.getElementById('offset-7').value = calib_data[7]['offset']
    document.getElementById('gain-7').value = calib_data[7]['gain']
}

function save_calib_data(){

	var calib_data = [
		{
			"offset": 0, 
			"gain": 0
		},
		{
			"offset": parseInt(document.getElementById('offset-1').value), 
			"gain": parseInt(document.getElementById('gain-1').value)
		},
		{
			"offset": parseInt(document.getElementById('offset-2').value), 
			"gain": parseInt(document.getElementById('gain-2').value)
		},
		{
			"offset": parseInt(document.getElementById('offset-3').value), 
			"gain": parseInt(document.getElementById('gain-3').value)
		},
		{
			"offset": parseInt(document.getElementById('offset-4').value), 
			"gain": parseInt(document.getElementById('gain-4').value)
		},
		{
			"offset": parseInt(document.getElementById('offset-5').value), 
			"gain": parseInt(document.getElementById('gain-5').value)
		},
		{
			"offset": parseInt(document.getElementById('offset-6').value), 
			"gain": parseInt(document.getElementById('gain-6').value)
		},
		{
			"offset": parseInt(document.getElementById('offset-7').value), 
			"gain": parseInt(document.getElementById('gain-7').value)
		},
	]

	eel.save_calib_data(calib_data)
}

// Index functions
function busca_escala(){
	return document.getElementById('escala-select').value
}


function solicita_resitencia(){
    eel.solicita_resitencia(busca_escala());
}


function remove_multiplier(value){
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

const CEM_MICRO = 0.0001
const UM_MILI	= 0.001
const DEZ_MILI = 0.01
const CEM_MILI = 0.1
const UM = 1
const DEZ = 10
const CEM = 100
const MIL = 1000
const DEZ_MIL = 10000

// <99.999u 	=	12.123u 	resistencia/1000000 + 3 casas
// <999.99u 	=	123.12u 	resistencia/1000000 + 2 casas
// <9.9999m 	=	1.1234m		resistencia/1000 + 4 casas
// <99.999m 	=	12.123m 	resistencia/1000 + 3 casas
// <999.99m 	=	123.12m 	resistencia/1000 + 2 casas
// <9.9999  	=	1.1234 		resistencia + 4 casas
// <99.999 		=	12.123 		resistencia + 3 casas
// <999.99 		=	123.12 		resistencia + 2 casas
// <9999.9 		=	1234.1  	resistencia + 1 casas
// >9999.9 		=	12345 		resistencia + 0 casas


function toFixed(value, precision) {
    var power = Math.pow(10, precision || 0);
    return String(Math.round(value * power) / power);
}


function add_multiplier(value) {
	if (value < CEM_MICRO){
		value = value * 1000000
		value = toFixed(value,3)
		return (value + 'uΩ')
	}
	else if (value < UM_MILI){
		value = value * 1000000
		value = toFixed(value,2)
		return (value + 'uΩ')
	}
	else if (value < DEZ_MILI){
		value = value * 1000
		value = toFixed(value,4)
		return (value + 'mΩ')
	} 
	else if (value < CEM_MILI){
		value = value * 1000
		value = toFixed(value,3)
		return (value + 'mΩ')
	}
	else if (value < UM){
		value = value * 1000
		value = toFixed(value,2)
		return (value + 'mΩ')
	}
	else if (value < DEZ){
		value = toFixed(value,4)
		return (value + 'Ω')
	}
	else if (value < CEM){
		value = toFixed(value,3)
		return (value + 'Ω')
	}
	else if (value < MIL){
		value = toFixed(value,2)
		return (value + 'Ω')
	}
	else if (value < DEZ_MIL){
		value = toFixed(value,1)
		return (value + 'Ω')
	}
	else {
		value = toFixed(value,0)
		return (value + 'Ω')
	}
}


function verifica_limites(){
	resistance_min = remove_multiplier(document.getElementById('Rmin').value)
	resistance_max = remove_multiplier(document.getElementById('Rmax').value)
	resistance_read = remove_multiplier(document.getElementById('resistance-field').value)
	
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


function recebe_resistencia(resistance_read){
	eel.pythonPrint(resistance_read)
	resistance_read = add_multiplier(resistance_read)
	eel.pythonPrint(resistance_read)
    document.getElementById('resistance-field').value = resistance_read
    verifica_limites()
}