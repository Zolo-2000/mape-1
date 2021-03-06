$(function () {
	//Initialize modals
	$('.modal').modal();
	$('.parallax').parallax();
	$('.carousel').carousel();
	$("#boton").sideNav({
		menuWidth: 300, // Default is 300
	      edge: 'right', // Choose the horizontal origin
	      closeOnClick: true, // Closes side-nav on <a> clicks, useful for Angular/Meteor
	      draggable: false, // Choose whether you can drag to open on touch screens,
	    }
	  );
	Materialize.updateTextFields(); 
	//Selects
	$(document).ready(function() {
	    $('select').material_select();
	});
	
	//Material datetimepicker
	datepickers = $('.datepicker');

	if (datepickers.length) {
		datepickers.pickadate({
		    selectMonths: true, // Creates a dropdown to control month
		    selectYears: 15, // Creates a dropdown of 15 years to control year
		    format:'dd/mm/yyyy',
		    today: 'Hoy',
		    clear: 'Limpiar',
		    close: 'Ok' 
		});	
	}

	timepickers = $('.timepicker');	

	if (timepickers.length) {
		timepickers.pickatime({
		    autoclose: false,
		    twelvehour: false,	 
		});	
	}

	//Init for select2

	if ($('.select2').select2) {
		$('.select2').select2({
			tags: true,
		})
	}

});
